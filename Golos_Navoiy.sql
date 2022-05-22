-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 22 2022 г., 15:56
-- Версия сервера: 5.6.37
-- Версия PHP: 5.5.38

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `Golos_Navoiy`
--

-- --------------------------------------------------------

--
-- Структура таблицы `application`
--

CREATE TABLE `application` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `application` varchar(700) NOT NULL,
  `answer_aplicate` varchar(225) NOT NULL DEFAULT 'None',
  `answer_doc` varchar(250) NOT NULL DEFAULT 'None',
  `date` varchar(12) NOT NULL,
  `end_date` date NOT NULL,
  `app_type` varchar(25) NOT NULL DEFAULT 'new'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `application`
--

INSERT INTO `application` (`id`, `user_id`, `application`, `answer_aplicate`, `answer_doc`, `date`, `end_date`, `app_type`) VALUES
(8, 315375144, 'iltimos manga qarab bering', 'фывфывфывфывфыв', 'None', '2022-05-16', '0000-00-00', 'reviewed'),
(9, 315375144, 'Iltimos sharoit qilib beringlar', 'salom mir....', 'None', '2022-05-16', '0000-00-00', 'reviewed'),
(11, 315375144, 'Qachon internet yaxshilanadi', 'Иди гуляй....', 'None', '2022-05-16', '0000-00-00', 'reviewed'),
(12, 315375144, 'iltimos tv ni taxlang', 'uchirib yoq!!!', 'None', '2022-05-16', '0000-00-00', 'review'),
(13, 315375144, 'Asalom aleykum manga svaz joq', 'Svaz juq bulganda, juq buladida...', 'None', '2022-05-22', '0000-00-00', 'review'),
(14, 315375144, 'Iltimos choy damlab beringlar', 'None', 'files/ReadMe_rus.doc', '2022-05-22', '0000-00-00', 'review'),
(15, 315375144, 'Пожалусто почините мой телефон', 'None', 'files/УТВЕРЖДАЮ.docx', '2022-05-22', '0000-00-00', 'review'),
(16, 315375144, 'suv tashkillashtiring iltimos managa judayam kerak', 'None', 'None', '2022-05-22', '0000-00-00', 'new');

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `fio` varchar(40) NOT NULL,
  `User_id` varchar(20) NOT NULL,
  `Phone` varchar(15) NOT NULL,
  `Adres` varchar(50) NOT NULL,
  `types` varchar(20) NOT NULL DEFAULT 'client'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `fio`, `User_id`, `Phone`, `Adres`, `types`) VALUES
(3, 'Aziz Nazarov', '1078736196', '+998907318801', 'uzbekistan 2-10', 'operator'),
(4, 'Hilola Xodjaeva', '315375144', '+998914157530', 'Uzbekiston2 -10', 'user');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `application`
--
ALTER TABLE `application`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `application`
--
ALTER TABLE `application`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;
--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
