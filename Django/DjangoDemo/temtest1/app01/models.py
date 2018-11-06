from django.db import models
from django.utils.translation import ugettext_lazy as _


class Customer(models.Model):

    name = models.CharField(_("Name"), max_length=200)
    updated = models.DateTimeField(_("Update"), auto_now=True)


    def __str__(self):
        return u'%s' % (self.name, )

class Apps(models.Model):

    displayName =   models.CharField(_("Display Name"), max_length=64, blank=True, null=True)
    packageName =   models.CharField(_("Package Name"), max_length=256, blank=True, null=True)


    def __str__(self):
        return u'%s_%s' % (self.displayName, self.version())


    class Meta:
        # 定义表名
        verbose_name        = _("My App")
        verbose_name_plural = _("My Apps")



class DeviceAppUpdate(models.Model):

    UID = models.CharField(_('UID'), max_length=18)
    customer = models.ForeignKey('Customer',blank=True, null=True,on_delete=models.CASCADE)
    app = models.ForeignKey('Apps',blank=True, null=True,on_delete=models.CASCADE)
    isUpdated = models.BooleanField(_("Is updated"),default=False)

    def __str__(self):
        return self.isUpdate

    class Meta:
         # 定义表名
        verbose_name        = _("Device App Update")
        verbose_name_plural = _("Device App Update")