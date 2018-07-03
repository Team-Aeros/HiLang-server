from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # Login
    path('login', views.login, name='login'),

    # Tokens
    path('checkToken', views.check_token, name='checkToken'),
    path('destroyToken', views.destroy_token, name='destroyToken'),

    # Users
    path('users/',views.get_users, name='users'),
    path('user/<int:user_id>/', views.get_user, name='user'),
    path('user/create/', views.create_user, name='create_user'),
    path('user/<int:user_id>/edituser/', views.edit_user, name='save_user'),
    path('user/distributor/', views.is_distributor, name='is_distributor'),

    # Courses
    path('courses/',views.get_courses, name='courses'),
    path('courses/public', views.get_public_courses, name='public_courses'),
    path('courses/<int:user_id>/', views.get_user_courses, name='user courses'),
    path('course/language/<int:language_id>/', views.get_course_lang, name='course_by_lang'),
    path('course/<int:course_id>/', views.get_course, name='course'),
    path('course/<int:course_id>/delete/', views.delete_course, name='delete_course'),
    path('course/create/', views.create_course, name='create_course'),
    path('course/<int:course_id>/edit_desc', views.edit_course_desc, name='edit_course_desc'),
    path('course/<int:course_id>/edit_lang', views.edit_course_lang, name='edit_course_lang'),
    path('course/search', views.search_courses,name="search_courses"),
    path('course/update/', views.update_course, name="update_course"),
    path('course/popular/', views.get_popular_courses, name="popular_courses"),
    path('course/newest/', views.get_newest_courses, name="newest_courses"),
    path('update_activity/', views.update_activity, name="update_activity"),
    path('last_accessed/', views.get_last_accessed, name="last_accessed"),

    # Lessons
    path('course/<int:course_id>/create-lesson', views.create_lesson, name='create_lesson'),
    path('course/<int:lesson_id>/get_questions', views.get_sentence_questions, name='get_questions'),
    path('lesson/<int:id>', views.get_lesson, name='lesson'),
    path('lesson/<int:id>/delete/', views.delete_lesson, name='lesson_delete'),
    path('course/<int:course_id>/lessons', views.get_course_lessons, name='course_lessons'),
    path('lesson/<int:id>/details', views.get_lesson_det, name='lesson_details'),
    path('lesson/<int:lesson_id>/edit_desc', views.edit_lesson_desc, name='edit_lesson_desc'),
    path('lessontypes', views.get_lesson_types, name='lesson_type'),
    path('lesson/<int:user_id>/<int:lesson_id>/completed', views.set_lesson_completed, name="lesson_completed"),
    path('lesson/<int:user_id>/getcompleted', views.get_completed_lessons, name="get_completed_lessons"),


    # Languages
    path('languages/', views.get_languages, name='languages'),
    path('language/<int:language_id>/', views.get_lang_details, name="lang_details"),
    path('course/<int:course_id>/languages', views.get_lang_course, name = "course_lang"),

    # Subscriptions
    path('user/subscriptions/<int:user_id>/', views.get_user_subscriptions, name='user_subscriptions'),
    path('course/subscriptions/<int:course_id>/', views.get_course_subscriptions, name='course_subscriptions'),
    path('course/subscribe', views.subscribe, name="subscribe"),
    path('course/unsubscribe', views.unsubscribe, name="unsubscribe"),

    # Favorite
    path('course/favorite', views.add_favorite, name='favorite'),
    path('course/unfavorite', views.del_favorite, name='unfavorite'),
    path('user/favorites/<int:user_id>/', views.get_user_favorites, name='user+favorites')
]

# integratie google, online woordenboek iets in die richting?
# Google translate uitspraak
