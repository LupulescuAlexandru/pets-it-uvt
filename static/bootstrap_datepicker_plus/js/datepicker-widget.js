jQuery(function(e){var t={},a="4"==e.fn.collapse.Constructor.VERSION.split(".").shift();function n(e,t){e.date&&t.val().length&&t.val(e.date.endOf("month").format("YYYY-MM-DD"))}e("[dp_config]:not([disabled])").each(function(n,d){var i=e(d),o={};try{o=JSON.parse(i.attr("dp_config"))}catch(e){}o.id&&o.options&&(o.$element=i.datetimepicker(o.options),o.datepickerdata=i.data("DateTimePicker"),t[o.id]=o,o.$element.next(".input-group-addon").on("click",function(){o.datepickerdata.show()}),a&&o.$element.on("dp.show",function(t){e(".collapse.in").addClass("show")}))}),e.each(t,function(e,a){if(a.linked_to){var d=t[a.linked_to];d.datepickerdata.maxDate(a.datepickerdata.date()||!1),a.datepickerdata.minDate(d.datepickerdata.date()||!1),d.$element.on("dp.change",function(e){a.datepickerdata.minDate(e.date||!1)}),a.$element.on("dp.change",function(e){"MONTH"==a.picker_type&&n(e,a.$element),d.datepickerdata.maxDate(e.date||!1)}),"MONTH"==a.picker_type&&(a.$element.on("dp.hide",function(e){n(e,a.$element)}),n({date:a.datepickerdata.date()},a.$element))}}),a&&(e("body").on("show.bs.collapse",".bootstrap-datetimepicker-widget .collapse",function(t){e(t.target).addClass("in")}),e("body").on("hidden.bs.collapse",".bootstrap-datetimepicker-widget .collapse",function(t){e(t.target).removeClass("in")}))});