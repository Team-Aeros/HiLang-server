﻿SET FOREIGN_KEY_CHECKS = 0;

INSERT INTO `api_course` (`id`, `name`, `description`, `user_id`, `image`, `subscribers`, `native_lang_id`, `trans_lang_id`, `public`, `created_at`) VALUES
(1, 'English for beginners', 'Learn to write English properly.', 1, 'http://www.linguapaths.com/wp-content/uploads/2016/09/regular-english-course-valencia.jpg', 0,2,1,1, '2018-06-22 08:07:39.827747'),
(2, 'French for beginners', 'Learn to speak French properly', 4, 'https://i.pinimg.com/originals/3a/14/f0/3a14f0325f7316ef603539116dae02ac.jpg', 0,2,3,0, '2018-06-22 08:07:39.827747'),
(3, 'German for beginners', 'Learn to write Germam properly', 4, 'https://www.imperial.ac.uk/ImageCropToolT4/imageTool/uploaded-images/deutsch-2--tojpeg_1437992131488_x2.jpg', 0,2,4,1, '2018-06-22 08:07:39.827747'),
(4, 'Peninsular Spanish for beginners', 'This course is meant for those who are interested in learning Spanish the way it is spoken in Spain.', 1, 'http://wallpoper.com/images/00/38/97/83/cityscapes-spain_00389783.jpg', 0, 1, 6, 1, '2018-06-22 08:07:39.827747');


INSERT INTO `api_language` (`id`, `name`, `flag`) VALUES
(1, 'English', 'england'),
(2, 'Dutch', 'netherlands'),
(3, 'German', 'germany'),
(4, 'French', 'france'),
(5, 'Russian', 'russia'),
(6, 'Spanish', 'spain'),
(7, 'Other',   '');

INSERT INTO `api_lesson` (`id`, `name`, `category`, `description`, `course_id`, `created_at`) VALUES
(1, 'Welcome to Spain', 'basic phrases', 'A quick introduction to the Spanish language.', 4, '2018-06-22 08:07:39.827747'),
(2, 'Making friends', 'friendship', 'In this lesson you will learn how to make friends.', 4, '2018-06-22 08:07:39.827747');


INSERT INTO `api_lessontype` (`id`, `name`, `description`) VALUES
(1, 'Grammar', 'Learn grammar'),
(2, 'Flashcards', 'Learn with flashcards'),
(3, 'Completion', 'Learn with completion exercises');

INSERT INTO `api_subscription` (`id`, `course_id`, `user_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 1, 3),
(4, 3, 1),
(5, 2, 3),
(6, 3, 2);

INSERT INTO `api_favorite` (`id`, `course_id`, `user_id`) VALUES
(1,1,1),
(2,2,1),
(3,1,3),
(4,3,1);

INSERT INTO `api_user` (`id`, `email`, `name`, `password`, `distributor`,`attempt`, `salt`, `created_at`, `avatar`) VALUES
(1, 'piet@hotmail.com', 'piet', '$2b$14$DCPL27eNDFgiZeirSdlkLezj6xPk1PxtEiWA2y81J82M1i76Pg9yy', 0,0, '$2b$14$lv3.j37BeHx5wOJP9E.H3e', '2018-06-22 08:07:39.827747', ''),
(2, 'jan@hotmail.com', 'jan', '$2b$14$KO0.3tK1D3U/pO/zL7TyDeiXZl4zUMzjP2re3wIslCJntgJkUvNpi', 1,0, '$2b$14$lv3.j37BeHx5wOJP9E.H3e', '2018-06-22 08:07:39.827747', ''),
(3, 'peter@hotmail.com', 'peter', '$2b$14$OPt82Ho/ObhUe/qFczelSuEDSiu30QEwBmiY/idztCd6tZqgnzivO', 0,0, '$2b$14$lv3.j37BeHx5wOJP9E.H3e', '2018-06-22 08:07:39.827747', ''),
(4, 'sara@hotmail.com', 'sara', '$2b$14$kg0GTLPopgoe/2o0dtz4jejfCgrjAn4e3feemd3//fBSItClD.ND.', 1,0, '$2b$14$lv3.j37BeHx5wOJP9E.H3e', '2018-06-22 08:07:39.827747', ''),
(5, 'evert@hotmail.com', 'evert', '$2b$14$oDwX/e6NmHnvzhwPWgCF4.8O9I4GXgc.QdUYZsR9LWS4RjlSFzz46', 0,0, '$2b$14$lv3.j37BeHx5wOJP9E.H3e', '2018-06-22 08:07:39.827747', '');


INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$kEJf41igeCuu$iHOT0wafWzt+SlSOD7N7iPdigUNx5bzVJfz5g8JPyR8=', '2018-05-30 08:00:26.447438', 1, 'root', '', '', 'bertde.boer@hotmail.com', 1, 1, '2018-05-30 07:59:58.949897');

INSERT INTO `api_wordlistquestion` (`id`, `native`, `translation`, `lesson_id`, `sentenceStructure`) VALUES
(1, 'Hello', 'Hola', 1,0),
(2, 'How are you? (informal)', '¿Qué tal?', 1,0),
(3, 'Spain', 'España', 1,0),
(4, 'I am twenty years old.', 'Tengo veinte años.', 1,0),
(5, 'Please', 'Por favor', 1,0),
(6, 'Thank you', 'Gracias', 1,0),
(7, 'Thank you very much', 'Muchas gracias', 1,0),
(8, 'Help me!', 'Ayúdame!', 1,0),
(9, 'A beer, please.', 'Una cerveza, por favor.', 1,0),
(10, 'Is there a supermarket nearby?', 'Hay un supermercado por aquí?', 1,0),
(11, 'What\'s your name?', '¿Cómo te llamas?', 2,0),
(12, 'Nice to meet you!', '¡Encantado!', 2,0),
(13, 'Would you like to go for a drink?', '¿Quieres tomar algo?', 2,0),
(14, 'Where do you live?', '¿Dónde vives?', 2,0),
(15, 'My name is Juan.', 'Me llamo Juan.', 2,0),
(16, 'I like movies.', 'Me gustan las películas.', 2,0),
(17, 'I\'m from France.', 'Soy de Francia.', 2,0),
(18, 'Catalonia is Spain.', 'Cataluña es España.', 2,0),
(19, 'I live in Amsterdam.', 'Vivo en Ámsterdam.', 2,0),
(20, 'What do you study?', '¿Qué estudias?', 2,0),
(21, 'Spanish is not my native language.', 'El castellano no es mi lengua materna.', 2,0);


SET FOREIGN_KEY_CHECKS = 1;