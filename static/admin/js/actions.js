!function(e){"use strict";var t;e.fn.actions=function(n){var a=e.extend({},e.fn.actions.defaults,n),o=e(this),s=!1,c=function(){e(a.acrossClears).hide(),e(a.acrossQuestions).show(),e(a.allContainer).hide()},i=function(){e(a.acrossClears).show(),e(a.acrossQuestions).hide(),e(a.actionContainer).toggleClass(a.selectedClass),e(a.allContainer).show(),e(a.counterContainer).hide()},l=function(){e(a.acrossClears).hide(),e(a.acrossQuestions).hide(),e(a.allContainer).hide(),e(a.counterContainer).show()},r=function(){l(),e(a.acrossInput).val(0),e(a.actionContainer).removeClass(a.selectedClass)},u=function(t){t?c():l(),e(o).prop("checked",t).parent().parent().toggleClass(a.selectedClass,t)},d=function(){var t=e(o).filter(":checked").length,n=e(".action-counter").data("actionsIcnt");e(a.counterContainer).html(interpolate(ngettext("%(sel)s of %(cnt)s selected","%(sel)s of %(cnt)s selected",t),{sel:t,cnt:n},!0)),e(a.allToggle).prop("checked",function(){var e;return t===o.length?(e=!0,c()):(e=!1,r()),e})};e(a.counterContainer).show(),e(this).filter(":checked").each(function(t){e(this).parent().parent().toggleClass(a.selectedClass),d(),1===e(a.acrossInput).val()&&i()}),e(a.allToggle).show().on("click",function(){u(e(this).prop("checked")),d()}),e("a",a.acrossQuestions).on("click",function(t){t.preventDefault(),e(a.acrossInput).val(1),i()}),e("a",a.acrossClears).on("click",function(t){t.preventDefault(),e(a.allToggle).prop("checked",!1),r(),u(0),d()}),t=null,e(o).on("click",function(n){n||(n=window.event);var s=n.target?n.target:n.srcElement;if(t&&e.data(t)!==e.data(s)&&!0===n.shiftKey){var c=!1;e(t).prop("checked",s.checked).parent().parent().toggleClass(a.selectedClass,s.checked),e(o).each(function(){e.data(this)!==e.data(t)&&e.data(this)!==e.data(s)||(c=!c),c&&e(this).prop("checked",s.checked).parent().parent().toggleClass(a.selectedClass,s.checked)})}e(s).parent().parent().toggleClass(a.selectedClass,s.checked),t=s,d()}),e("form#changelist-form table#result_list tr").on("change","td:gt(0) :input",function(){s=!0}),e('form#changelist-form button[name="index"]').on("click",function(e){if(s)return confirm(gettext("You have unsaved changes on individual editable fields. If you run an action, your unsaved changes will be lost."))}),e('form#changelist-form input[name="_save"]').on("click",function(t){var n=!1;if(e("select option:selected",a.actionContainer).each(function(){e(this).val()&&(n=!0)}),n)return s?confirm(gettext("You have selected an action, but you haven't saved your changes to individual fields yet. Please click OK to save. You'll need to re-run the action.")):confirm(gettext("You have selected an action, and you haven't made any changes on individual fields. You're probably looking for the Go button rather than the Save button."))})},e.fn.actions.defaults={actionContainer:"div.actions",counterContainer:"span.action-counter",allContainer:"div.actions span.all",acrossInput:"div.actions input.select-across",acrossQuestions:"div.actions span.question",acrossClears:"div.actions span.clear",allToggle:"#action-toggle",selectedClass:"selected"},e(document).ready(function(){var t=e("tr input.action-select");t.length>0&&t.actions()})}(django.jQuery);