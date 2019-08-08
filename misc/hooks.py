# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "misc"
app_title = "Misc"
app_publisher = "Ebuka Akeru "
app_description = "Random functionality based on ERPNext"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ebukaakeru@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/misc/css/misc.css"
# app_include_js = "/assets/misc/js/misc.js"

# include js, css files in header of web template
# web_include_css = "/assets/misc/css/misc.css"
# web_include_js = "/assets/misc/js/misc.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Item" : "public/js/sample.js",

	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "misc.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "misc.install.before_install"
# after_install = "misc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "misc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"misc.tasks.all"
# 	],
# 	"daily": [
# 		"misc.tasks.daily"
# 	],
# 	"hourly": [
# 		"misc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"misc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"misc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "misc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "misc.event.get_events"
# }

