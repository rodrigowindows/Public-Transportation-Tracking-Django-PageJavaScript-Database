from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rytmuv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myproject.view.welcome', name='welcome'),
    url(r'^GET_insertCompany', 'myproject.view.GET_insertCompany'),
    url(r'^GET_selectACompany', 'myproject.view.GET_selectACompany'),
    url(r'^GET_selectAllCompany', 'myproject.view.GET_selectAllCompany'),
    url(r'^GET_insertBus', 'myproject.view.GET_insertBus'),
    url(r'^GET_selectAbus', 'myproject.view.GET_selectAbus'),
    url(r'^GET_selectbusFromCompany', 'myproject.view.GET_selectbusFromCompany'),
    url(r'^GET_selectbusFromRoute', 'myproject.view.GET_selectbusFromRoute'),
    url(r'^GET_insertgeoPosition', 'myproject.view.GET_insertgeoPosition'),
    url(r'^GET_selectLastGeoPosition', 'myproject.view.GET_selectLastGeoPosition'),
    url(r'^GET_insertRoute', 'myproject.view.GET_insertRoute'),
    url(r'^GET_selectARoute', 'myproject.view.GET_selectARoute'),
    url(r'^GET_insert_BusStop', 'myproject.view.GET_insert_BusStop'),
    url(r'^GET_selectABusStop', 'myproject.view.GET_selectABusStop'),
    url(r'^GET__insert_BusStop_has_route', 'myproject.view.GET__insert_BusStop_has_route'),
    url(r'^GET_selectBusStop_has_route_busStop', 'myproject.view.GET_selectBusStop_has_route_busStop'),
    url(r'^GET_selectBusStop_has_route_route_id', 'myproject.view.GET_selectBusStop_has_route_route_id'),
    url(r'^GET_selectAWeekDay', 'myproject.view.GET_selectAWeekDay'),
    url(r'^GET_insertWeekDay', 'myproject.view.GET_insertWeekDay'),
    url(r'^GET_selectAllWeekDay', 'myproject.view.GET_selectAllWeekDay'),
    url(r'^GET__insert_scheduleRouteatBusStop', 'myproject.view.GET__insert_scheduleRouteatBusStop'),
    url(r'^GET_selectAScheduleRouteatBusStop', 'myproject.view.GET_selectAScheduleRouteatBusStop'),
    url(r'^GET_selectscheduleRouteatBusStop_route', 'myproject.view.GET_selectscheduleRouteatBusStop_route'),
    url(r'^GET_selectscheduleRouteatBusStop_busStop', 'myproject.view.GET_selectscheduleRouteatBusStop_busStop'),
    url(r'^GET_getBusTimeAtBusStop', 'myproject.view.GET_getBusTimeAtBusStop'),
)
