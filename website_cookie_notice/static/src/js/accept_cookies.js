/* © 2015 Antiun Ingeniería, S.L.
 * © 2015 Lorenzo Battistini - Agile Business Group
 * License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
 */

odoo.define('website_cookie_notice.cookie_notice', function (require) {
    "use strict";

    var base = require('web_editor.base');

    base.ready().done(function() {
        $(".cc-cookies .btn-primary").click(function(e) {
            e.preventDefault();
            document.cookie = 'accepted_cookies=1; path=/';
            $(e.target).closest(".cc-cookies").hide("fast");
        });
    });
}
);
