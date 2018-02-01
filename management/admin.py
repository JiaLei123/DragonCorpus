# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import rrt_project,rrt_domain,rrt_audio,rrt_utterance,rrt_intent,rrt_testsuit,rrt_project_test_case,rrt_slot,rrt_baseline_test_case,rrt_project_running_test_case,rrt_account
# Register your models here.

# class rrt_project_Admin(admin.ModelAdmin):
#     list_display = ('id','project_name', 'project_description','create_time','modify_time','creater')
#
# class rrt_domain_Admin(admin.ModelAdmin):
#     list_display = ('id','domain_name')
#
# class rrt_audio_Admin(admin.ModelAdmin):
#     list_display = ('id','audio_path','speaker','gender','format','create_time')
#
# class rrt_utterance_Admin(admin.ModelAdmin):
#     list_display = ('id','utterance','audio_id','gloable_priority')
#
# class rrt_intent_Admin(admin.ModelAdmin):
#     list_display = ('id','intent_name','','')
#
# class rrt_testsuit_Admin(admin.ModelAdmin):
#     list_display = ('id','testsuit_name','create_time')
#
# class rrt_project_test_case_Admin(admin.ModelAdmin):
#     list_display = ('id','project_id','domain_id','utterance_id','intent_id','case_priority','select_times','select_flag','testsuit_id')
#
# class rrt_slot_Admin(admin.ModelAdmin):
#     list_display = ('id','slot_names','slot_values')
#
# class rrt_baseline_test_case_Admin(admin.ModelAdmin):
#     list_display = ('id','project_test_case_id','utterance_id','case_priority','select_times','select_flag')
#
# class rrt_project_running_test_case_Admin(admin.ModelAdmin):
#     list_display = ('id','baseline_test_case_id','project_id','domain_id','utterance_id','intent_id','log_id','create_time','testsuit_id')
#
# class rrt_account_Admin(admin.ModelAdmin):
#     list_display = ('id','user_name','user_password')
#
# admin.site.register(rrt_domain, rrt_domain_Admin)
# admin.site.register(rrt_project, rrt_project_Admin)
# admin.site.register(rrt_audio, rrt_audio_Admin)
# admin.site.register(rrt_utterance, rrt_utterance_Admin)
# admin.site.register(rrt_intent, rrt_intent_Admin)
# admin.site.register(rrt_testsuit, rrt_testsuit_Admin)
# admin.site.register(rrt_project_test_case, rrt_project_test_case_Admin)
# admin.site.register(rrt_slot, rrt_slot_Admin)
# admin.site.register(rrt_baseline_test_case, rrt_baseline_test_case_Admin)
# admin.site.register(rrt_project_running_test_case, rrt_project_running_test_case_Admin)
# admin.site.register(rrt_account, rrt_account_Admin)