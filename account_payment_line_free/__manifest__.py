##############################################################################
#
#       ______ Releasing children from poverty      _
#      / ____/___  ____ ___  ____  ____ ___________(_)___  ____
#     / /   / __ \/ __ `__ \/ __ \/ __ `/ ___/ ___/ / __ \/ __ \
#    / /___/ /_/ / / / / / / /_/ / /_/ (__  |__  ) / /_/ / / / /
#    \____/\____/_/ /_/ /_/ .___/\__,_/____/____/_/\____/_/ /_/
#                        /_/
#                            in Jesus' name
#
#    Copyright (C) 2014-2019 Compassion CH (http://www.compassion.ch)
#    @author: Simon Gonzalez <simon.gonzalez@bluewin.ch>, Emanuel Cino
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# pylint: disable=C8101
{
    "name": "Account payment line free",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "Compassion Suisse",
    "website": "https://github.com/CompassionCH/test-repo",
    "category": "Banking addons",
    "depends": ["account_payment_order"],
    "data": [
        "views/invoice_view.xml",
        "views/account_payment_order_view.xml",
        "views/account_payment_line_view.xml",
    ],
    "installable": True,
}
