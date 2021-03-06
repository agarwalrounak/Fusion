from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

app_name = 'office'

urlpatterns = [

    url(r'^officeOfDeanPnD/submit$',views.submitRequest,name='pWorkRequest'),
    url(r'^officeOfDeanPnD/action$',views.action,name='action'),
    url(r'^officeOfPurchaseOfficer/',views.officeOfPurchaseOfficer, name ='officeOfPurchaseOfficer'),
    url(r'^apply_purchase/', views.apply_purchase, name='apply_purchase'),
    url(r'^after_purchase/', views.after_purchase, name='after_purchase'),
    url(r'^officeOfRegistrar/$', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^officeOfDeanRSPC/$', views.officeOfDeanRSPC, name='officeOfDeanRSPC'),

    url(r'^officeOfDeanRSPC/submit/$',views.project_register,name='p_register'),
    url(r'^officeOfDeanRSPC/extention/$',views.project_extension,name='p_extension'),
    url(r'^officeOfDeanRSPC/close/$',views.project_closure,name='p_closure'),
    url(r'^officeOfDeanRSPC/reallocate/$',views.project_reallocation,name='p_reallocation'),
    url(r'^officeOfDeanRSPC/action/$',views.project_registration_permission, name='registration'),
    url(r'^officeOfDeanRSPC/extension/$',views.project_extension_permission,name='extension'),
    url(r'^officeOfDeanRSPC/closure/$',views.project_closure_permission,name='closure'),
    url(r'^officeOfDeanRSPC/reallocation/$',views.project_reallocation_permission,name='reallocation'),
    url(r'^officeOfDeanRSPC/forwarded/$',views.hod_action,name='hod_action'),
    url(r'^officeOfDeanRSPC/forwarded1/$',views.hod_closure,name='hod_closure'),
    url(r'^officeOfDeanRSPC/forwarded2/$',views.hod_extension,name='hod_extension'),
    url(r'^officeOfDeanRSPC/forwarded3/$',views.hod_allocation,name='hod_allocation'),
    url(r'^officeOfDeanRSPC/registration_details/(?P<pr_id>[0-9]+)/$',views.reg_details,name='reg_details'),
    url(r'^officeOfDeanRSPC/extension_details/(?P<pr_id>[0-9]+)/$',views.ext_details,name='ext_details'),
    url(r'^officeOfDeanRSPC/closure_details/(?P<pr_id>[0-9]+)/$',views.closure_details,name='closure_details'),
    url(r'^officeOfDeanRSPC/reallocation_details/(?P<pr_id>[0-9]+)/$',views.reallocate_details,name='reallocate_details'),

    url(r'^eisModulenew/profile', views.eisModulenew, name='eisModulenew'),

    url(r'^officeOfDeanPnD/$', views.officeOfDeanPnD, name='officeOfDeanPnD'),
    url(r'^officeOfHOD/$', views.officeOfHOD, name='officeOfHOD'),
    url(r'^officeOfHOD/submit/$',views.teaching_form,name='teaching_form'),
    url(r'^officeOfHOD/work/$',views.hod_work,name='hod_work'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^deleteitem/(?P<id>[0-9]+)',views.delete_item, name='delete_item'),
    url(r'^deletevendor/(?P<id>[0-9]+)',views.delete_vendor, name='delete_vendor'),
    url(r'^editvendor/(?P<id>[0-9]+)',views.edit_vendor, name='edit_vendor'),
    url(r'^editvendor/office/officeOfPurchaseOfficer/edit/',views.edit,name='edit'),
    url(r'^edititem/(?P<id>[0-9]+)',views.edit_item, name='edit_item'),
    url(r'^edititem/office/officeOfPurchaseOfficer/edit1/',views.edit1,name='edit'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^directorOffice/$', views.directorOffice, name='directorOffice'),
    url(r'^directorOffice/appoint', views.appoint, name='appoint'),
    url(r'^directorOffice/meeting', views.meeting, name='meeting'),
    url(r'^officeOfRegistrar/upload/$', views.upload, name='upload'),
    url(r'^officeOfRegistrar/generalAdminForm/reject/$', csrf_exempt(views.admin_reject), name='admin_reject'),
    url(r'^officeOfDeanStudents/$', views.officeOfDeanStudents, name='officeOfDeanStudents'),
    url(r'^officeOfPurchaseOfficer/', views.officeOfPurchaseOfficr, name='officeOfPurchaseOfficer'),
    url(r'^officeOfRegistrar/', views.officeOfRegistrar, name='officeOfRegistrar'),
    url(r'^genericModule/', views.genericModule, name='genericModule'),
    url(r'^officeOfDeanStudents/holding_meeting', views.holdingMeeting, name='holdingMeetings'),
    url(r'^officeOfDeanStudents/meeting_Minutes', views.meetingMinutes, name='meetingMinutes'),
    url(r'^officeOfDeanStudents/hostelRoomAllotment', views.hostelRoomAllotment),
    url(r'^officeOfDeanStudents/budget_approval', views.budgetApproval),
    url(r'^officeOfDeanStudents/budget_rejection', views.budgetRejection),
    url(r'^officeOfDeanStudents/club_approval', views.clubApproval),
    url(r'^officeOfDeanStudents/club_rejection', views.clubRejection),
    url(r'^officeOfDeanStudents/budgetAllot', views.budgetAllot),
    url(r'^officeOfDeanStudents/budgetAllotEdit', views.budgetAllotEdit),
    url(r'^officeOfDeanAcademics/$', views.officeOfDeanAcademics, name='officeOfDeanAcademics'),

    url(r'^officeOfDeanAcademics/assistantship', views.assistantship, name='assistantship'),
    url(r'^officeOfDeanAcademics/formsubmit', views.formsubmit, name='formsubmit'),
    url(r'^officeOfDeanAcademics/init_assistantship', views.init_assistantship, name='init_assistantship'),
    url(r'^officeOfDeanAcademics/scholarshipform', views.scholarshipform),
    url(r'^officeOfDeanAcademics/applications', views.applications, name='applications'),
    url(r'^officeOfDeanAcademics/courses', views.courses, name='courses'),
    url(r'^officeOfDeanAcademics/scholarship', views.scholarship, name='scholarship'),
    url(r'^officeOfDeanAcademics/semresults', views.semresults, name='semresults'),
    url(r'^officeOfDeanAcademics/thesis', views.thesis, name='thesis'),
]
