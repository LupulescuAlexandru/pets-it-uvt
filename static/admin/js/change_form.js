!function(e){"use strict";e(document).ready(function(){var t=e("#django-admin-form-add-constants").data("modelName");e("body").on("click",".add-another",function(t){t.preventDefault();var n=e.Event("django:add-another-related");e(this).trigger(n),n.isDefaultPrevented()||showAddAnotherPopup(this)}),t&&e("form#"+t+"_form :input:visible:enabled:first").focus()})}(django.jQuery);