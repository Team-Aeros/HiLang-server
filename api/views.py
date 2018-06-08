import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.contrib.auth import authenticate, login
import json
import string
import random
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from api.models import *

<<<<<<< HEAD
def index(request):
    return HttpResponse("Dit is een API")
=======
>>>>>>> upstream/master

def generate_token():
    alphabet = string.ascii_letters + string.digits
    while True:
        return ''.join(random.SystemRandom().choice(alphabet) for i in range(60))


def validate_token(userId, token):
    try:
        user = User.objects.get(pk=userId)
        userTokens = Token.objects.filter(user=user)
        for userToken in userTokens:
            if (userToken.token == token):
                if (user.attempt > 0):
                    user.attempt = 0
                    user.save()
                return True
    except ObjectDoesNotExist:
        return False
    user.attempt += 1
    if (user.attempt >= 5):
        destroy_user_tokens(userId)
    else:
        user.save()
    return False

def parse_params(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        if (validate_token(data['user_id', 'token'])):
            return data['params']
    return None

def check_token(request):
    if (request.method == 'POST'):
        if (request.body):
            data = json.loads(request.body.decode('utf-8'))
            return JsonResponse({'approved': validate_token(data['user_id'], data['token'])}, safe=False)
    return JsonResponse({'approved': False}, safe=False)


def destroy_token(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(pk=data['user_id'])
            token = Token.objects.get(token=data['token'], user=user).delete()
        except ObjectDoesNotExist:
            pass


def destroy_user_tokens(user_id):
    user = User.objects.get(pk=user_id)
    user.attempt = 0
    user.save()
    Token.objects.filter(user=user).delete()


def get_json_response(serialize):
    return HttpResponse(serialize, content_type='application/json')


def index(request):
    return HttpResponse("Dit is een API")


# Login
def login(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        try:
            user = User.objects.get(email=data['email'], password=data['password'])
            token = Token(token=generate_token(), user=user)
            token.save()
            response = {
                        'user_id': user.pk,
                        'token': token.token
                        }
            return JsonResponse(response, safe=False)
        except ObjectDoesNotExist:
            pass
    return JsonResponse({}, safe=False)

# Users
def get_users(request):
    return get_json_response(serializers.serialize('json', User.objects.all()))

def get_user(request, user_id):
    return get_json_response(serializers.serialize('json', User.objects.filter(id=user_id)))

def create_user(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        user = User(email=data['email'], name=data['name'], password=data['password'], distributor=0)
        try:
            user.save()
            return get_json_response(serializers.serialize('json', [user]))
        except IntegrityError as e:
            return get_json_response(serializers.serialize('json', []))


# Courses
def get_courses(request):
    # data = parse_params(request);
    # if (data == None):
    #     return HttpResponseForbidden();
    return get_json_response(serializers.serialize('json', Course.objects.all()))


def get_course(request, course_id, user_id):
    courseData = Course.objects.get(id=course_id)
    authorData = User.objects.get(pk=user_id)
    favoriteData = Favorite.objects.filter(user=authorData, course=Course.objects.get(pk=course_id))
    subscriptionData = Subscription.objects.filter(user=authorData, course=Course.objects.get(pk=course_id))
    if not favoriteData:
        favorite = False
    else:
        favorite = True

    if not subscriptionData:
        subscription = False
    else:
        subscription = True

    returnData = {
        'id': courseData.id,
        'name': courseData.name,
        'author': authorData.name,
        'authorId': courseData.user.pk,
        'description': courseData.description,
        'image': courseData.image,
        'favorite': favorite,
        'subscription': subscription
    }
    return JsonResponse(returnData)


def get_public_courses(request):
    return get_json_response(serializers.serialize('json', Course.objects.filter(public=1)))


def get_course_lang(request, language_id):
    return get_json_response(serializers.serialize('json', Course.objects.filter(language=language_id)))


def create_course(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user = User.objects.get(pk=data['user'])
        course = Course(name=data['name'], user=user)
        course.save()
        return get_json_response(serializers.serialize('json', [course]))


def get_user_courses(request, user_id):
    courseData = Course.objects.filter(user=User.objects.get(pk=user_id))
    return get_json_response(serializers.serialize('json', courseData))


def edit_course_desc(request, course_id):
    course = Course.objects.get(pk=course_id)
    data = json.loads(request.body.decode('utf-8'))
    course.description = data['desc']
    course.save()
    return HttpResponse(request)


def search_courses(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        courseData = Course.objects.filter(name__icontains=data['name'], public=1)
        returnData = []
        for course in courseData:
            author = course.user
            returnData.append(
                {
                    "id": course.id,
                    "name": course.name,
                    "description": course.description,
                    "image": course.image,
                    "subscribers": course.subscribers,
                    "author": author.name
                }
            )
        return JsonResponse(returnData, safe=False)


# Lessons

def create_lesson(request, course_id):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        course = Course.objects.get(pk=course_id)
        lesson = Lesson(name=data['title'],
                        category=data['category'],
                        description=data['description'],
                        grammar=data['grammar'],
                        course=course)
        lesson.save()
        for question, answer in data['words'].items():
            entry = WordListQuestion(native=question, translation=answer, lesson=lesson)
            entry.save()
        return get_json_response(serializers.serialize('json', [lesson]))


def get_lesson(request, id):
    lesson = list(Lesson.objects.filter(pk=id).values())
    lesson[0]['vocabulary'] = list(WordListQuestion.objects.filter(lesson=id).values())

    return HttpResponse(json.dumps(lesson), content_type='application/json')


def delete_lesson(request, id):
    if request.method == 'DELETE':
        lesson = Lesson.objects.get(pk=id)
        lesson.delete(4)
        return HttpResponse()


def get_course_lessons(request, course_id):
    lessonData = Lesson.objects.filter(course_id=course_id)
    return get_json_response(serializers.serialize('json', lessonData))


def get_lesson_det(request, id):
    lessonData = Lesson.objects.get(pk=id)
    courseData = Course.objects.get(pk=lessonData.course_id)
    nativeData = Language.objects.get(pk=courseData.native_lang.id)
    transData = Language.objects.get(pk=courseData.trans_lang.id)
    returnData = {
        "id": lessonData.id,
        "name": lessonData.name,
        "cat": lessonData.category,
        "desc": lessonData.description,
        "native": nativeData.name,
        "trans": transData.name
    }
    return JsonResponse(returnData)


def edit_lesson_desc(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    data = json.loads(request.body.decode('utf-8'))
    lesson.description = data['desc']
    lesson.save()
    return HttpResponse(request)


# Languages
def get_languages(request):
    return get_json_response(serializers.serialize('json', Language.objects.all()))


def get_lang_details(request, language_id):
    return get_json_response(serializers.serialize('json', Language.objects.filter(id=language_id)))


# Subscriptions
def get_user_subscriptions(request, user_id):
    subscriptionData = serializers.serialize('json', Subscription.objects.filter(user=User.objects.get(pk=user_id)))
    data = json.loads(subscriptionData)
    returnData = []
    for sub in data:
        course_id = sub['fields']['course']
        courseData = Course.objects.get(pk=course_id)
        returnData.append(courseData)
    return get_json_response(serializers.serialize('json', returnData))


def get_course_subscriptions(request, course_id):
    return get_json_response(serializers.serialize('json', Subscription.objects.filter(course=course_id)))


def subscribe(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        Subscription.objects.create(user=User.objects.get(pk=data['user']),
                                    course=Course.objects.get(pk=data['course']))
    return get_json_response(request)


def unsubscribe(request):
    if (request.method == 'POST'):
        data = json.loads(request.body.decode('utf-8'))
        entry = Subscription.objects.filter(user=User.objects.get(pk=data['user']),
                                            course=Course.objects.get(pk=data['course']))
        entry.delete()
    return get_json_response(request)


# Favorite
def add_favorite(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        Favorite.objects.create(user=User.objects.get(pk=data['user']), course=Course.objects.get(pk=data['course']))
    return get_json_response(request)


def del_favorite(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        entry = Favorite.objects.filter(user=User.objects.get(pk=data['user']),
                                        course=Course.objects.get(pk=data['course']))
        entry.delete()
    return get_json_response(request)


def get_user_favorites(request, user_id):
    favoriteData = serializers.serialize('json', Favorite.objects.filter(user=User.objects.get(pk=user_id)))
    data = json.loads(favoriteData)
    returnData = []
    for fav in data:
        course_id = fav['fields']['course']
        courseData = Course.objects.get(pk=course_id)
        returnData.append(courseData)
    return get_json_response(serializers.serialize('json', returnData))
