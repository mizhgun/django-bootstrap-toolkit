# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView
import demo_app.views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    url(r'^form$', demo_app.views.demo_form, name='demo_app.views.demo_form'),
    url(r'^form_template$', demo_app.views.demo_form_with_template, name='demo_app.views.demo_form_with_template'),
    url(r'^form_inline$', demo_app.views.demo_form_inline, name='demo_app.views.demo_form_inline'),
    url(r'^formset$', demo_app.views.demo_formset, {}, name="formset"),
    url(r'^tabs$', demo_app.views.demo_tabs, {}, name="tabs"),
    url(r'^pagination$', demo_app.views.demo_pagination, {}, name="pagination"),
    url(r'^widgets$', demo_app.views.demo_widgets, {}, name="widgets"),
    url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
]
