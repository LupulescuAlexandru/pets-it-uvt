!function(e){"use strict";var d=e("#django-admin-prepopulated-fields-constants").data("prepopulatedFields");e.each(d,function(d,a){e(".empty-form .form-row .field-"+a.name+", .empty-form.form-row .field-"+a.name).addClass("prepopulated_field"),e(a.id).data("dependency_list",a.dependency_list).prepopulate(a.dependency_ids,a.maxLength,a.allowUnicode)})}(django.jQuery);