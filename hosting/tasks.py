from celery import shared_task
from celery.utils.log import get_task_logger
from opennebula_api.models import OpenNebulaManager
from utils.mailer import BaseEmail
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

logger = get_task_logger(__name__)


@shared_task
def delete_vm_task(user, vm, base_url=None):
    """
    Deletes a specified vm by a user
    :param user: The user object containing the email and password
    :param vm: The VM object that is to be deleted
    :return: True if the task is successful, False otherwise
    """
    logger.info("Executing delete VM task: VM.id={}, user.email={}".format(vm.id, user.email))
    manager = OpenNebulaManager(
        email=user.email,
        password=user.password
    )
    terminated = manager.delete_vm(vm.id)

    if not terminated:
        logger.error(
            'Error terminating VM {}'.format(vm.id)
        )
    else:
        context = {
            'vm': vm,
            'base_url': base_url
        }
        email_data = {
            'subject': _('Virtual machine plan canceled'),
            'from_address': settings.DCL_SUPPORT_FROM_ADDRESS,
            'to': user.email,
            'context': context,
            'template_name': 'vm_status_changed',
            'template_path': 'hosting/emails/'
        }
        email = BaseEmail(**email_data)
        email.send()
    return terminated


@shared_task
def add(x, y):
    return x + y
