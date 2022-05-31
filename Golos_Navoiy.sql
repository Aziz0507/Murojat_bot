-- phpMyAdmin SQL Dump
-- version 4.7.3
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Май 31 2022 г., 07:59
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
  `app_type` varchar(25) NOT NULL DEFAULT 'new',
  `app_button` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `application`
--

INSERT INTO `application` (`id`, `user_id`, `application`, `answer_aplicate`, `answer_doc`, `date`, `end_date`, `app_type`, `app_button`) VALUES
(8, 315375144, 'iltimos manga qarab bering', 'фывфывфывфывфыв', 'None', '2022-05-16', '0000-00-00', 'reviewed', ''),
(9, 315375144, 'Iltimos sharoit qilib beringlar', 'salom mir....', 'None', '2022-05-16', '0000-00-00', 'reviewed', ''),
(11, 315375144, 'Qachon internet yaxshilanadi', 'Иди гуляй....', 'None', '2022-05-16', '0000-00-00', 'reviewed', ''),
(12, 315375144, 'iltimos tv ni taxlang', 'uchirib yoq!!!', 'None', '2022-05-16', '0000-00-00', 'review', ''),
(13, 315375144, 'Asalom aleykum manga svaz joq', 'Svaz juq bulganda, juq buladida...', 'None', '2022-05-22', '0000-00-00', 'review', ''),
(14, 315375144, 'Iltimos choy damlab beringlar', 'None', 'files/ReadMe_rus.doc', '2022-05-22', '0000-00-00', 'review', ''),
(15, 315375144, 'Пожалусто почините мой телефон', 'None', 'files/УТВЕРЖДАЮ.docx', '2022-05-22', '0000-00-00', 'review', ''),
(16, 315375144, 'suv tashkillashtiring iltimos managa judayam kerak', 'None', 'None', '2022-05-22', '0000-00-00', 'new', ''),
(17, 315375144, 'Iltimos rengeni teshing', 'None', 'None', '2022-05-23', '0000-00-00', 'new', ''),
(18, 722188816, 'Нимага навои телевидиянинг камралари хира тасвирга олади', 'None', 'files/стихи о родине.doc', '2022-05-23', '0000-00-00', 'review', ''),
(19, 387713426, 'Konime', 'None', 'None', '2022-05-27', '0000-00-00', 'new', ''),
(20, 387713426, 'Tomdi', 'None', 'None', '2022-05-27', '0000-00-00', 'new', ''),
(21, 387713426, 'Konimasd', 'None', 'None', '2022-05-27', '0000-00-00', 'new', ''),
(22, 387713426, 'Konimasid', 'None', 'None', '2022-05-27', '0000-00-00', 'new', ''),
(23, 387713426, 'Konmakon', 'None', 'None', '2022-05-27', '0000-00-00', 'new', ''),
(24, 315375144, 'asdasdasdasd', 'None', 'None', '2022-05-28', '0000-00-00', 'new', ''),
(25, 315375144, 'Konimex', 'None', 'None', '2022-05-28', '0000-00-00', 'new', ''),
(26, 315375144, 'Konimes', 'None', 'None', '2022-05-28', '0000-00-00', 'new', ''),
(27, 315375144, 'Koshin', 'None', 'None', '2022-05-28', '0000-00-00', 'new', ''),
(28, 315375144, 'asdasdasdasdasd', 'None', 'None', '2022-05-28', '0000-00-00', 'new', '');

-- --------------------------------------------------------

--
-- Структура таблицы `mobil_baza`
--

CREATE TABLE `mobil_baza` (
  `id` int(11) NOT NULL,
  `Viloyat` varchar(100) NOT NULL,
  `Tuman` varchar(100) NOT NULL,
  `Axoli_punkt` varchar(100) NOT NULL,
  `reja_mobile` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `mobil_baza`
--

INSERT INTO `mobil_baza` (`id`, `Viloyat`, `Tuman`, `Axoli_punkt`, `reja_mobile`) VALUES
(3, 'Навоий вилояти', 'Конимех', 'Баймурат овули ', '22-23'),
(4, 'Навоий вилояти', 'Конимех', 'Қалмурат қазған овули', '22-23'),
(5, 'Навоий вилояти', 'Конимех', 'Учтепа овули ', '22-23'),
(6, 'Навоий вилояти', 'Конимех', 'Есқудуқ овули ', '23'),
(7, 'Навоий вилояти', 'Конимех', 'Териқудуқ овули', '23'),
(8, 'Навоий вилояти', 'Конимех', 'Уразжан овули ', '23'),
(9, 'Навоий вилояти', 'Конимех', 'Балакарак овули ', '22-23'),
(10, 'Навоий вилояти', 'Конимех', 'Караката  ', '22'),
(11, 'Навоий вилояти', 'Конимех', ' Дунгалак овули ', '22'),
(12, 'Навоий вилояти', 'Конимех', 'Пахтакор овули', '22'),
(13, 'Навоий вилояти', 'Конимех', 'Фидокор овули (Прике)', '22'),
(14, 'Навоий вилояти', 'Конимех', 'Янги турмуш овули', '23'),
(15, 'Навоий вилояти', 'Конимех', 'Қосқудуқ овули ', '23'),
(16, 'Навоий вилояти', 'Конимех', 'Талдиқудуқ овули', '23'),
(17, 'Навоий вилояти', 'Конимех', 'Кенгдала қишлоғи   (Испанқудуқ)', '23'),
(18, 'Навоий вилояти', 'Конимех', 'Бесқудуқ овули ', '23'),
(19, 'Навоий вилояти', 'Конимех', 'Кенбайкудук овули ', '23'),
(20, 'Навоий вилояти', 'Конимех', 'Порлоқ овули ст', '23'),
(21, 'Навоий вилояти', 'қизилтепа т.', 'Янгиобод', '22'),
(22, 'Навоий вилояти', 'қизилтепа т.', 'Маликчўл', '22'),
(23, 'Навоий вилояти', 'қизилтепа т.', 'Шейхон', '22'),
(24, 'Навоий вилояти', 'қизилтепа т.', 'Арабхона', '23'),
(25, 'Навоий вилояти', 'томди т.', 'Актакир  ', '23'),
(26, 'Навоий вилояти', 'томди т.', 'Керизбулок овули', '22'),
(27, 'Навоий вилояти', 'томди т.', 'Угизтов овули', '22'),
(28, 'Навоий вилояти', 'томди т.', 'Жириқ овули', '23'),
(29, 'Навоий вилояти', 'томди т.', 'Утемурат овули', '22'),
(30, 'Навоий вилояти', 'томди т.', 'Қизилқудуқ  ', '23'),
(31, 'Навоий вилояти', 'томди т.', 'Алдаберген  а.п.', '23'),
(32, 'Навоий вилояти', 'томди т.', 'Шимбай  а.п.', '23'),
(33, 'Навоий вилояти', 'томди т.', 'Кулимбет  а.п.', '23'),
(34, 'Навоий вилояти', 'томди т.', 'Нурмахон  а.п.', '23'),
(35, 'Навоий вилояти', 'учқудуқ т.', 'Алтинтов', '22'),
(36, 'Навоий вилояти', 'учқудуқ т.', 'Узунқудуқ овули ', '22'),
(37, 'Навоий вилояти', 'учқудуқ т.', 'Бузоқбай овули ', '22'),
(38, 'Навоий вилояти', 'учқудуқ т.', 'Кукаяз ОФЙ ', '22'),
(39, 'Навоий вилояти', 'нурота т.', 'Самари  ', '23'),
(40, 'Навоий вилояти', 'нурота т.', 'Шомуродчорбоғ ', '23'),
(41, 'Навоий вилояти', 'нурота т.', 'Болташовдир ', '23'),
(42, 'Навоий вилояти', 'нурота т.', 'Улус ', '23'),
(43, 'Навоий вилояти', 'нурота т.', 'Қўзибойқудуқ ', '23'),
(44, 'Навоий вилояти', 'нурота т.', 'Кўктепа', '23'),
(45, 'Навоий вилояти', 'нурота т.', 'Зулқайнар ', '23'),
(46, 'Навоий вилояти', 'нурота т.', 'Кичиксой', '22-23'),
(47, 'Навоий вилояти', 'нурота т.', 'Соб', '23'),
(48, 'Навоий вилояти', 'нурота т.', 'Модувот  ', '23'),
(49, 'Навоий вилояти', 'нурота т.', 'Совуқбулоқ ', '23'),
(50, 'Навоий вилояти', 'хатирчи т.', 'Ўртаовул ', '23'),
(51, 'Навоий вилояти', 'хатирчи т.', 'Юзовул ', '23'),
(52, 'Навоий вилояти', 'хатирчи т.', 'Дўрмон', '23'),
(53, 'Навоий вилояти', 'хатирчи т.', 'Сарой ', '23'),
(54, 'Навоий вилояти', 'хатирчи т.', 'Ангидон ', '23'),
(55, 'Навоий вилояти', 'хатирчи т.', 'Шалдироқ', '23'),
(56, 'Навоий вилояти', 'хатирчи т.', 'Қуврай ', '23'),
(57, 'Навоий вилояти', 'хатирчи т.', 'Тошбулоқ ', '23'),
(58, 'Навоий вилояти', 'хатирчи т.', 'Мингёнғоқ ', '23'),
(59, 'Навоий вилояти', 'хатирчи т.', 'Тариқпоя ', '23'),
(60, 'Навоий вилояти', 'хатирчи т.', 'Ёнғоқли', '23'),
(61, 'Навоий вилояти', 'хатирчи т.', 'Оча майли', '23'),
(62, 'Навоий вилояти', 'хатирчи т.', 'Қўнғирот', '23'),
(63, 'Навоий вилояти', 'хатирчи т.', 'Чинор', '23'),
(64, 'Навоий вилояти', 'хатирчи т.', 'Олтинсой', '23'),
(65, 'Навоий вилояти', 'хатирчи т.', 'Олмоти ', '23'),
(66, 'Навоий вилояти', 'хатирчи т.', 'Оқтовуз', '23'),
(67, 'Навоий вилояти', 'хатирчи т.', 'Хонақа ', '23'),
(68, 'Навоий вилояти', 'хатирчи т.', 'Бурқут', '23'),
(69, 'Навоий вилояти', 'хатирчи т.', 'Қўчқорчи ', '23'),
(70, 'Навоий вилояти', 'хатирчи т.', 'Кориз аччи ', '23'),
(71, 'Навоий вилояти', 'хатирчи т.', 'Кориз', '23'),
(72, 'Навоий вилояти', 'хатирчи т.', 'Хилвоши', '23'),
(73, 'Навоий вилояти', 'хатирчи т.', 'Бахшижар МФЙ', '23'),
(74, 'Навоий вилояти', 'Кармана т.', '\"Малик махалласи, Қалдирғоч массив \"', '23'),
(75, 'Навоий вилояти', 'Навбаҳор т.', '\"Янгиобод МФЙ,Анорбоғи\"', '23');

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
(9, 'Madjidova Kamilla Alisherovna', '722188816', '+998906657298', 'Navoiy shahar', 'user'),
(12, 'Qurbonov Akmal', '387713426', '998973226755', 'Konimex tumani porloq ovuli', 'user'),
(14, 'Xilola Xodjaeva', '315375144', '+998914157530', 'uzbekistan 2 10', 'user');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `application`
--
ALTER TABLE `application`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `mobil_baza`
--
ALTER TABLE `mobil_baza`
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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT для таблицы `mobil_baza`
--
ALTER TABLE `mobil_baza`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;
--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
