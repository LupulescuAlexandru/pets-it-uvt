!function(){"use strict";var r=[{re:/^\d{1,2}$/i,handler:function(r){return 1===r[0].length?"0"+r[0]+":00":r[0]+":00"}},{re:/^\d{2}[:.]\d{2}$/i,handler:function(r){return r[0].replace(".",":")}},{re:/^\d[:.]\d{2}$/i,handler:function(r){return"0"+r[0].replace(".",":")}},{re:/^(\d+)\s*([ap])(?:.?m.?)?$/i,handler:function(r){var e=parseInt(r[1]);return 12===e&&(e=0),"p"===r[2].toLowerCase()?(12===e&&(e=0),e+12+":00"):e<10?"0"+e+":00":e+":00"}},{re:/^(\d+)[.:](\d{2})\s*([ap]).?m.?$/i,handler:function(r){var e=parseInt(r[1]),n=parseInt(r[2]);return n<10&&(n="0"+n),12===e&&(e=0),"p"===r[3].toLowerCase()?(12===e&&(e=0),e+12+":"+n):e<10?"0"+e+":"+n:e+":"+n}},{re:/^no/i,handler:function(r){return"12:00"}},{re:/^mid/i,handler:function(r){return"00:00"}}];window.parseTimeString=function(e){for(var n=0;n<r.length;n++){var t=r[n].re,a=r[n].handler,i=t.exec(e);if(i)return a(i)}return e}}();