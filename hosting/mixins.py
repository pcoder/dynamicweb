from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from opennebula_api.serializers import VirtualMachineTemplateSerializer
from opennebula_api.models import OpenNebulaManager

from .models import HostingPlan
import logging

logger = logging.getLogger(__name__)


class ProcessVMSelectionMixin(object):
    def post(self, request, *args, **kwargs):
        type_error = False
        try:
            template_id = int(request.POST.get('vm_template_id'))
            configuration_id = int(request.POST.get('configuration'))
            template = OpenNebulaManager().get_template(template_id)
            data = VirtualMachineTemplateSerializer(template).data
            configuration = HostingPlan.objects.get(id=configuration_id)

            request.session['template'] = data
            request.session['specs'] = configuration.serialize()
        except TypeError as te:
            logger.debug(
                "Type error in ProcessVMSelectionMixin. Details: {}".format(
                    str(te)))
            type_error = True

        if not request.user.is_authenticated() or type_error:
            request.session['next'] = reverse('hosting:payment')
            return redirect(reverse('hosting:login'))
        return redirect(reverse('hosting:payment'))
