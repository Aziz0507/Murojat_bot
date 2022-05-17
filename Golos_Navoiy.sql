-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 17 2022 г., 20:23
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
  `answer_doc` varchar(55) NOT NULL DEFAULT 'None',
  `date` varchar(12) NOT NULL,
  `end_date` date NOT NULL,
  `app_type` varchar(45) NOT NULL DEFAULT 'new'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `application`
--

INSERT INTO `application` (`id`, `user_id`, `application`, `answer_aplicate`, `answer_doc`, `date`, `end_date`, `app_type`) VALUES
(1, 1078736196, 'iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz', 'sizga yaxshi sharoit qilinadi', 'None', '12-04-2022', '0000-00-00', 'new'),
(2, 1078736196, 'siz registraciyadan alla qachon utgan siz', 'sizga yaxshi sharoit qilinadi', 'None', '14-98-2478', '0000-00-00', 'new'),
(3, 1078736196, 'TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz', 'sizga yaxshi sharoit qilinadi', 'None', '78-96-5412', '0000-00-00', 'new'),
(4, 1078736196, 'sizning arizangiz qabul qilindi, va yaqin orada biz javob berishga harakat qilamiz//////////////////', 'sizga yaxshi sharoit qilinadi', 'None', '36-98-25', '0000-00-00', 'new'),
(5, 1078736196, 'datetimedatetimedatetimedatetimedatetimedatetimedatetimedatetime', 'sizga yaxshi sharoit qilinadi', 'None', '2022-04-28', '0000-00-00', 'new'),
(6, 1078736196, 'datetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimedatetimeasdasdasssssssssssssssss', 'sizga yaxshi sharoit qilinadi', 'None', '2022-04-28', '0000-00-00', 'new'),
(7, 1078736196, 'asdasfhghjoikljnrifjdksgfhnueklhdfjmxadsfafasdasd', 'sizga yaxshi sharoit qilinadi', 'None', '2022-04-28', '0000-00-00', 'new'),
(8, 315375144, 'iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz//////////////////////////////////////////////////////////////////', 'sizga yaxshi sharoit qilinadi', 'None', '2022-4-30', '0000-00-00', 'new'),
(9, 315375144, 'iltimos qiynagan savolingizni bravering, yaqin orada biz javob berishga harakat qilamiz//////////////////////////////////////////////////////////////////asdasdasdasdasdasd', 'sizga yaxshi sharoit qilinadi', 'None', '2022-4-30', '0000-00-00', 'new'),
(10, 315375144, 'asldgaslhgdalsfglasfgladhgfladshgflsdhagflsdhfgjhsgfsldhfgsldhfgslhfgslhdfgslhdfgslfgsldhfgsdhjkgfsjhkdgfsjdhfgsjhdfglshdfglshdgflskdjhlkjhgflskjhdflskdhgfashalskdbxcnbvlajgflkdfbnlhfdlkd', 'sizga yaxshi sharoit qilinadi', 'None', '2022-4-30', '0000-00-00', 'new'),
(11, 315375144, 'Qachon yollar yaxshilanadi', 'None', 'None', '2022-5-17', '0000-00-00', 'new');

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
(4, 'Xilola Xodjaeva', '315375144', '+998914157530', 'uzbekisrtan 2-10', 'user');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
