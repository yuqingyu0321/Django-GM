-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: management
-- ------------------------------------------------------
-- Server version	5.7.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=58 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(7,'Can add permission',3,'add_permission'),(8,'Can change permission',3,'change_permission'),(9,'Can delete permission',3,'delete_permission'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add 框',7,'add_bgslideovermodel'),(20,'Can change 框',7,'change_bgslideovermodel'),(21,'Can delete 框',7,'delete_bgslideovermodel'),(22,'Can add Icon布局',8,'add_gridslideovermodel'),(23,'Can change Icon布局',8,'change_gridslideovermodel'),(24,'Can delete Icon布局',8,'delete_gridslideovermodel'),(25,'Can add 位置设定',9,'add_positionmodel'),(26,'Can change 位置设定',9,'change_positionmodel'),(27,'Can delete 位置设定',9,'delete_positionmodel'),(28,'Can add 侧拉框',10,'add_slideovermodel'),(29,'Can change 侧拉框',10,'change_slideovermodel'),(30,'Can delete 侧拉框',10,'delete_slideovermodel'),(31,'Can add 拉按钮',11,'add_pullslideovermodel'),(32,'Can change 拉按钮',11,'change_pullslideovermodel'),(33,'Can delete 拉按钮',11,'delete_pullslideovermodel'),(34,'Can add 导出游戏',12,'add_gameslideovermodel'),(35,'Can change 导出游戏',12,'change_gameslideovermodel'),(36,'Can delete 导出游戏',12,'delete_gameslideovermodel'),(37,'Can add 导出游戏',13,'add_gameiconswitchmodel'),(38,'Can change 导出游戏',13,'change_gameiconswitchmodel'),(39,'Can delete 导出游戏',13,'delete_gameiconswitchmodel'),(40,'Can add 导流条',14,'add_stripmodel'),(41,'Can change 导流条',14,'change_stripmodel'),(42,'Can delete 导流条',14,'delete_stripmodel'),(43,'Can add Icon切换',15,'add_iconswitchmodel'),(44,'Can change Icon切换',15,'change_iconswitchmodel'),(45,'Can delete Icon切换',15,'delete_iconswitchmodel'),(46,'Can add 标题',16,'add_labelslideovermodel'),(47,'Can change 标题',16,'change_labelslideovermodel'),(48,'Can delete 标题',16,'delete_labelslideovermodel'),(49,'Can add 导出游戏',17,'add_gamestripmodel'),(50,'Can change 导出游戏',17,'change_gamestripmodel'),(51,'Can delete 导出游戏',17,'delete_gamestripmodel'),(52,'Can add 文本',18,'add_textslideovermodel'),(53,'Can change 文本',18,'change_textslideovermodel'),(54,'Can delete 文本',18,'delete_textslideovermodel'),(55,'Can add 文件上传',19,'add_uploadmodel'),(56,'Can change 文件上传',19,'change_uploadmodel'),(57,'Can delete 文件上传',19,'delete_uploadmodel');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$36000$5SRqxM2sdoct$ByWt6OiUo0gDI7+f8Ry/KQ9wKmW8HoDZqbTlPINXgkM=','2019-04-01 16:19:11.363610',1,'admin','','','',1,1,'2019-03-05 19:38:09.369911'),(2,'pbkdf2_sha256$36000$Al9dXOAz9CVE$OS5ODgyPSO/p2Q4rgc/lCCxF8xLtuSiwu21A+eaJ824=','2019-03-29 17:53:55.804946',0,'yu','','','',1,1,'2019-03-05 19:47:00.000000'),(3,'pbkdf2_sha256$36000$iYvFc03cbvlm$/jZZHKHoWugWUnTyGtkaMPKPyBPjveAizjhPFEf3QGo=','2019-03-08 11:04:00.000000',0,'cuijiuling','','','',1,1,'2019-03-08 11:03:00.000000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
INSERT INTO `auth_user_user_permissions` VALUES (1,2,19),(2,2,20),(3,2,21),(4,2,22),(5,2,23),(6,2,24),(7,2,25),(8,2,26),(9,2,27),(10,2,28),(11,2,29),(12,2,30),(13,2,31),(14,2,32),(15,2,33),(16,2,34),(17,2,35),(18,2,36),(19,2,37),(20,2,38),(21,2,39),(22,2,40),(23,2,41),(24,2,42),(25,2,43),(26,2,44),(27,2,45),(28,2,46),(29,2,47),(30,2,48),(31,2,49),(32,2,50),(33,2,51),(34,2,52),(35,2,53),(36,2,54),(78,2,55),(76,2,56),(77,2,57),(37,3,19),(38,3,20),(39,3,21),(40,3,22),(41,3,23),(42,3,24),(43,3,25),(44,3,26),(45,3,27),(46,3,28),(47,3,29),(48,3,30),(49,3,31),(50,3,32),(51,3,33),(52,3,34),(53,3,35),(54,3,36),(55,3,37),(56,3,38),(57,3,39),(58,3,40),(59,3,41),(60,3,42),(61,3,43),(62,3,44),(63,3,45),(64,3,46),(65,3,47),(66,3,48),(67,3,49),(68,3,50),(69,3,51),(70,3,52),(71,3,53),(72,3,54),(75,3,55),(73,3,56),(74,3,57);
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=52 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-03-05 19:47:20.256938','2','yu',1,'[{\"added\": {}}]',4,1),(2,'2019-03-05 19:47:46.884210','2','yu',2,'[{\"changed\": {\"fields\": [\"is_staff\", \"user_permissions\"]}}]',4,1),(3,'2019-03-05 19:49:04.911336','1','3D涂色迷宫',1,'[{\"added\": {}}, {\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,2),(4,'2019-03-05 20:48:45.010690','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"changed\": {\"fields\": [\"position_id\", \"type\", \"x\", \"y\"], \"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,2),(5,'2019-03-05 20:52:07.001489','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(6,'2019-03-05 20:57:12.675245','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(7,'2019-03-05 21:03:50.434342','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(8,'2019-03-05 21:05:15.695977','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(9,'2019-03-05 21:06:45.820619','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u9014\\u6e38\\u4f11\\u95f2\\u6355\\u9c7c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(10,'2019-03-05 21:08:05.899841','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u4fc4\\u7f57\\u65af\\u65b9\\u5757\\u6d88\\u9664\\u4f20\\u5947\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(11,'2019-03-05 21:09:42.450247','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u6b22\\u4e50\\u5207\\u6c34\\u679c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(12,'2019-03-05 21:11:00.058978','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"\\u7956\\u739b\\u5f39\\u7403\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(13,'2019-03-05 21:12:11.278786','1','3D涂色迷宫',2,'[{\"added\": {\"object\": \"3D\\u7403\\u7403\\u6253\\u7816\\u5757\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(14,'2019-03-06 21:34:10.160960','1','3D涂色迷宫',1,'[{\"added\": {}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u9014\\u6e38\\u4f11\\u95f2\\u6355\\u9c7c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u4fc4\\u7f57\\u65af\\u65b9\\u5757\\u6d88\\u9664\\u4f20\\u5947\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u5207\\u6c34\\u679c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u7956\\u739b\\u5f39\\u7403\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"3D\\u7403\\u7403\\u6253\\u7816\\u5757\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',14,1),(15,'2019-03-07 16:52:05.228025','1','3D涂色迷宫',2,'[]',14,2),(16,'2019-03-07 17:53:34.770855','2','3D涂色迷宫',1,'[{\"added\": {}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u9014\\u6e38\\u4f11\\u95f2\\u6355\\u9c7c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u4fc4\\u7f57\\u65af\\u65b9\\u5757\\u6d88\\u9664\\u4f20\\u5947\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u5207\\u6c34\\u679c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u7956\\u739b\\u5f39\\u7403\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"3D\\u7403\\u7403\\u6253\\u7816\\u5757\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',14,2),(17,'2019-03-07 17:53:44.649333','2','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"version\"]}}]',14,2),(18,'2019-03-07 17:53:49.503181','2','3D涂色迷宫',3,'',14,2),(19,'2019-03-07 21:39:54.002616','2','3D涂色迷宫',1,'[{\"added\": {}}, {\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u9014\\u6e38\\u4f11\\u95f2\\u6355\\u9c7c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u4fc4\\u7f57\\u65af\\u65b9\\u5757\\u6d88\\u9664\\u4f20\\u5947\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u5207\\u6c34\\u679c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u7956\\u739b\\u5f39\\u7403\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"3D\\u7403\\u7403\\u6253\\u7816\\u5757\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,2),(20,'2019-03-07 21:40:06.657455','2','3D涂色迷宫',2,'[]',15,2),(21,'2019-03-08 10:23:00.487864','2','3D涂色迷宫',3,'',15,1),(22,'2019-03-08 10:52:13.601362','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"type\", \"x\", \"y\"], \"object\": \"\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,1),(23,'2019-03-08 11:03:40.350515','3','cuijiuling',1,'[{\"added\": {}}]',4,1),(24,'2019-03-08 11:03:59.877826','3','cuijiuling',2,'[{\"changed\": {\"fields\": [\"is_staff\", \"user_permissions\"]}}]',4,1),(25,'2019-03-09 17:05:59.867705','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',15,2),(26,'2019-03-09 17:06:15.006905','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',14,2),(27,'2019-03-09 18:25:06.230682','1','3D涂色迷宫',2,'[]',15,2),(28,'2019-03-09 18:27:34.631973','1','3D涂色迷宫',2,'[]',14,3),(29,'2019-03-09 22:30:16.193516','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}]',15,3),(30,'2019-03-11 16:31:37.276043','1','3D涂色迷宫',2,'[]',15,3),(31,'2019-03-12 21:57:37.918020','1','旅行小西瓜',1,'[{\"added\": {}}, {\"added\": {\"object\": \"\\u80cc\\u666f\\u6846\", \"name\": \"\\u80cc\\u666f\\u6846\"}}]',10,2),(32,'2019-03-12 21:57:56.466853','1','旅行小西瓜',3,'',10,2),(33,'2019-03-13 19:03:21.339636','3','cuijiuling',2,'[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]',4,1),(34,'2019-03-13 19:03:34.392938','2','yu',2,'[{\"changed\": {\"fields\": [\"user_permissions\", \"last_login\"]}}]',4,1),(35,'2019-03-13 19:04:35.961758','1','3D涂色迷宫',1,'[{\"added\": {}}]',19,2),(36,'2019-03-14 21:06:27.420076','1','3D涂色迷宫',3,'',19,2),(37,'2019-03-15 11:47:19.453984','1','祖玛弹球',1,'[{\"added\": {}}]',19,3),(38,'2019-03-15 11:52:40.668282','2','祖玛弹球',3,'',14,2),(39,'2019-03-15 11:58:12.338789','3','祖玛弹球',3,'',14,2),(40,'2019-03-15 20:07:08.621657','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}]',14,3),(41,'2019-03-15 20:08:09.446497','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}, {\"changed\": {\"fields\": [\"y\"], \"object\": \"1\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,3),(42,'2019-03-15 20:12:33.361643','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}, {\"changed\": {\"fields\": [\"y\"], \"object\": \"1\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,3),(43,'2019-03-15 20:12:43.996157','1','3D涂色迷宫',2,'[]',14,3),(44,'2019-03-15 20:15:50.998886','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"y\"], \"object\": \"1\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,3),(45,'2019-03-15 20:16:11.802935','1','3D涂色迷宫',2,'[]',14,3),(46,'2019-03-15 20:18:20.168504','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}]',14,3),(47,'2019-03-15 20:19:41.298729','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"y\"], \"object\": \"1\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}]',15,3),(48,'2019-03-15 20:52:46.112783','1','3D涂色迷宫',2,'[{\"changed\": {\"fields\": [\"framesInterval\"]}}]',14,3),(49,'2019-03-19 17:03:56.950371','2','3D涂色迷宫',1,'[{\"added\": {}}, {\"added\": {\"object\": \"4\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"5\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"6\", \"name\": \"\\u4f4d\\u7f6e\\u8bbe\\u5b9a\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u9014\\u6e38\\u4f11\\u95f2\\u6355\\u9c7c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u4fc4\\u7f57\\u65af\\u65b9\\u5757\\u6d88\\u9664\\u4f20\\u5947\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u6b22\\u4e50\\u5207\\u6c34\\u679c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"\\u7956\\u739b\\u5f39\\u7403\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"added\": {\"object\": \"3D\\u7403\\u7403\\u6253\\u7816\\u5757\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,1),(50,'2019-03-19 17:04:17.547455','2','疯狂枪手',2,'[{\"changed\": {\"fields\": [\"name\", \"game_id\", \"socket_url\"]}}, {\"deleted\": {\"object\": \"\\u75af\\u72c2\\u67aa\\u624b\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"deleted\": {\"object\": \"\\u6b22\\u4e50\\u9493\\u9c7c\\u5927\\u5e08\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"deleted\": {\"object\": \"\\u6570\\u5b57\\u6ce1\\u6ce1\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"deleted\": {\"object\": \"\\u738b\\u56fd\\u65e0\\u654c\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}, {\"deleted\": {\"object\": \"\\u75af\\u72c2\\u65a7\\u5934\", \"name\": \"\\u5bfc\\u51fa\\u6e38\\u620f\"}}]',15,1),(51,'2019-03-19 17:06:28.013471','2','疯狂枪手',3,'',15,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','group'),(3,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'oriented','bgslideovermodel'),(13,'oriented','gameiconswitchmodel'),(12,'oriented','gameslideovermodel'),(17,'oriented','gamestripmodel'),(8,'oriented','gridslideovermodel'),(15,'oriented','iconswitchmodel'),(16,'oriented','labelslideovermodel'),(9,'oriented','positionmodel'),(11,'oriented','pullslideovermodel'),(10,'oriented','slideovermodel'),(14,'oriented','stripmodel'),(18,'oriented','textslideovermodel'),(6,'sessions','session'),(19,'upload','uploadmodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-03-05 19:37:55.844192'),(2,'auth','0001_initial','2019-03-05 19:37:56.281583'),(3,'admin','0001_initial','2019-03-05 19:37:56.382983'),(4,'admin','0002_logentry_remove_auto_add','2019-03-05 19:37:56.421355'),(5,'contenttypes','0002_remove_content_type_name','2019-03-05 19:37:56.542307'),(6,'auth','0002_alter_permission_name_max_length','2019-03-05 19:37:56.607767'),(7,'auth','0003_alter_user_email_max_length','2019-03-05 19:37:56.671983'),(8,'auth','0004_alter_user_username_opts','2019-03-05 19:37:56.704269'),(9,'auth','0005_alter_user_last_login_null','2019-03-05 19:37:56.782362'),(10,'auth','0006_require_contenttypes_0002','2019-03-05 19:37:56.786369'),(11,'auth','0007_alter_validators_add_error_messages','2019-03-05 19:37:56.812773'),(12,'auth','0008_alter_user_username_max_length','2019-03-05 19:37:56.888525'),(13,'oriented','0001_initial','2019-03-05 19:37:57.256974'),(14,'oriented','0002_remove_gameiconswitchmodel_index','2019-03-05 19:37:57.294461'),(15,'oriented','0003_auto_20190227_1216','2019-03-05 19:37:58.044739'),(16,'oriented','0004_auto_20190305_1937','2019-03-05 19:37:58.102287'),(17,'sessions','0001_initial','2019-03-05 19:37:58.141236'),(18,'oriented','0002_auto_20190307_1635','2019-03-07 16:35:58.724108'),(19,'oriented','0002_auto_20190307_1644','2019-03-07 16:45:45.352271'),(20,'oriented','0002_auto_20190307_1738','2019-03-07 17:39:10.680678'),(21,'oriented','0003_auto_20190307_1740','2019-03-07 17:40:55.205147'),(22,'oriented','0004_auto_20190307_2124','2019-03-07 21:24:21.294519'),(23,'oriented','0005_auto_20190308_1049','2019-03-08 10:49:07.856572'),(24,'oriented','0006_auto_20190309_1704','2019-03-09 17:04:21.182551'),(25,'oriented','0007_auto_20190309_1824','2019-03-09 18:24:38.836011'),(26,'oriented','0008_auto_20190309_1830','2019-03-09 18:30:56.364144'),(27,'oriented','0009_auto_20190311_1630','2019-03-11 16:30:17.605595'),(28,'oriented','0010_auto_20190312_2155','2019-03-12 21:55:37.866702'),(29,'upload','0001_initial','2019-03-13 19:02:20.550389'),(30,'oriented','0011_auto_20190315_1157','2019-03-15 11:58:03.069731');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('2agmkp99kqlp1329n04rgcrsg63hmvqz','NGRmZTQ4ZGFhMTcxODBkNWY0OWRlZGY3Y2FlODFjM2VjMTUzYTU0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwMjY5OTc3MGQ1YTE4OWY5OGY3YjZlNTlhY2QxN2FlYmI2YzIyYWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-03-19 20:09:15.218379'),('4vvmdnpxzjsxm13c09hycifph91ji38z','NGRmZTQ4ZGFhMTcxODBkNWY0OWRlZGY3Y2FlODFjM2VjMTUzYTU0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwMjY5OTc3MGQ1YTE4OWY5OGY3YjZlNTlhY2QxN2FlYmI2YzIyYWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-04-15 16:19:11.372085'),('h0rfvw2kgigougdt97fm3yea8xktlxdp','NGRmZTQ4ZGFhMTcxODBkNWY0OWRlZGY3Y2FlODFjM2VjMTUzYTU0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwMjY5OTc3MGQ1YTE4OWY5OGY3YjZlNTlhY2QxN2FlYmI2YzIyYWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-04-08 15:37:30.541576'),('myganmp67d2rnr6xhlkj4d5e5h6n5x0v','NGRmZTQ4ZGFhMTcxODBkNWY0OWRlZGY3Y2FlODFjM2VjMTUzYTU0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwMjY5OTc3MGQ1YTE4OWY5OGY3YjZlNTlhY2QxN2FlYmI2YzIyYWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-03-29 15:47:52.929315'),('uu1vrxhny4nm48zor4d9q48e5gbmjdyf','MzQ5NTlmNjg2YTViZWYwYTkwZmYwZDgwNzdkMDdmZDE0MDY2YjE5YTp7Il9hdXRoX3VzZXJfaGFzaCI6IjEyNmQ3N2U0N2MwOTVlNjJmOTBjYTZmZjkzZjYxMTZiNWQ0Mzg1MjkiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIzIn0=','2019-03-22 11:04:09.630616'),('xwepqqv3t7knc4qj0a9mui67sr0vqhbc','NGRmZTQ4ZGFhMTcxODBkNWY0OWRlZGY3Y2FlODFjM2VjMTUzYTU0Yjp7Il9hdXRoX3VzZXJfaGFzaCI6IjUwMjY5OTc3MGQ1YTE4OWY5OGY3YjZlNTlhY2QxN2FlYmI2YzIyYWYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2019-03-20 10:37:49.057191');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_bgslideovermodel`
--

DROP TABLE IF EXISTS `oriented_bgslideovermodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_bgslideovermodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `foreignkey_labelSlideOver_id` int(11) NOT NULL,
  `bt_height` int(10) unsigned NOT NULL,
  `bt_imgurl` varchar(512) NOT NULL,
  `bt_scale` double NOT NULL,
  `bt_yfromtop` int(10) unsigned NOT NULL,
  `icon_iconsHeight` int(11) NOT NULL,
  `icon_iconsWidth` int(11) NOT NULL,
  `icon_paddingLeft` int(11) NOT NULL,
  `icon_paddingRight` int(11) NOT NULL,
  `icon_spacingX` int(11) NOT NULL,
  `icon_spacingY` int(11) NOT NULL,
  `kuang_bottomBlkHeight` int(10) unsigned NOT NULL,
  `kuang_imgurl` varchar(512) NOT NULL,
  `kuang_positionY` double NOT NULL,
  `la_imgurl0` varchar(512) NOT NULL,
  `la_imgurl1` varchar(512) NOT NULL,
  `la_isredon` tinyint(1) NOT NULL,
  `la_positionX` double NOT NULL,
  `la_positionY` double NOT NULL,
  `la_scale` double NOT NULL,
  `text_colorB` int(10) unsigned NOT NULL,
  `text_colorG` int(10) unsigned NOT NULL,
  `text_colorR` int(10) unsigned NOT NULL,
  `text_size` int(10) unsigned NOT NULL,
  `text_yfromIcon` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `foreignkey_labelSlideOver_id` (`foreignkey_labelSlideOver_id`),
  CONSTRAINT `oriented_bgslideover_foreignkey_labelSlid_3a78a65b_fk_oriented_` FOREIGN KEY (`foreignkey_labelSlideOver_id`) REFERENCES `oriented_slideovermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_bgslideovermodel`
--

LOCK TABLES `oriented_bgslideovermodel` WRITE;
/*!40000 ALTER TABLE `oriented_bgslideovermodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `oriented_bgslideovermodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_gameiconswitchmodel`
--

DROP TABLE IF EXISTS `oriented_gameiconswitchmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_gameiconswitchmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wxAppId` varchar(20) NOT NULL,
  `weight` int(10) unsigned NOT NULL,
  `scale` double NOT NULL,
  `imgLink` varchar(512) NOT NULL,
  `openType` tinyint(1) NOT NULL,
  `clickHide` tinyint(1) NOT NULL,
  `topath` varchar(512) NOT NULL,
  `bi_iconId` varchar(255) NOT NULL,
  `bi_landing_page` varchar(512) NOT NULL,
  `bi_landing_page_id` varchar(255) NOT NULL,
  `bi_educe_game` varchar(255) NOT NULL,
  `foreignkey_iconswitch_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oriented_gameiconswi_foreignkey_iconswitc_36b6aa0d_fk_oriented_` (`foreignkey_iconswitch_id`),
  CONSTRAINT `oriented_gameiconswi_foreignkey_iconswitc_36b6aa0d_fk_oriented_` FOREIGN KEY (`foreignkey_iconswitch_id`) REFERENCES `oriented_iconswitchmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_gameiconswitchmodel`
--

LOCK TABLES `oriented_gameiconswitchmodel` WRITE;
/*!40000 ALTER TABLE `oriented_gameiconswitchmodel` DISABLE KEYS */;
INSERT INTO `oriented_gameiconswitchmodel` VALUES (1,'wxaa5c62c26ee49681',20,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/qiangshou.png',1,0,'?from=3Dtsmg&togame=fkqs','1512','https://sanxqn.nalrer.cn/tysanxiao/linkImages/1.png','728','fkqs',1),(2,'wx57f49f44206958e6',20,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/diaoyu.png',1,0,'?from=3Dtsmg&togame=hldyds','1515','https://sanxqn.nalrer.cn/tysanxiao/happyfishmaster/linkpage.jpg','729','hldyds',1),(3,'wxdb030d1934b15d67',10,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/szpp.png',1,0,'?from=3Dtsmg&togame=szpp','1522','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/szpp1.jpg','735','szpp',1),(4,'wx656cf75188e899bf',10,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/wudi.png',1,0,'?from=3Dtsmg&togame=wgwd','1521','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/wgwd.jpg','734','wgwd',1),(5,'wxd7062438a8b82506',10,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/fkft.png',1,0,'?from=3Dtsmg&togame=fkft','1523','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox6.jpg','736','fkft',1),(6,'wx30efe34580243475',10,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/tyxxbuyu.png',1,0,'?from=3Dtsmg&togame=tyxxby','1519','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/tyxxbuyu.jpg','737','tyxxby',1),(7,'wx7a2ecd52309f2466',40,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/russiaxccq.png',1,0,'?from=3Dtsmg&togame=elsfkxccq','1516','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox11.jpg','730','elsfkxccq',1),(8,'wxa3855d93c407a5b6',30,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/hlqsg.png',1,0,'?from=3Dtsmg&togame=hlqsgds','1517','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox9.jpg','731','hlqsgds',1),(9,'wx81df03575e1e351f',20,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/zumatq.png',1,0,'?from=3Dtsmg&togame=zmtq','1520','https://sanxqn.nalrer.cn/tysanxiao/linkImages/zuma.png','733','zmtq',1),(10,'wxde9361a6865997fc',20,0.75,'https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/3Dqq.png',1,0,'?from=3Dtsmg&togame=3Dqqdzk','1518','https://sanxqn.nalrer.cn/tysanxiao/fireball/linkimg_3D.png','732','3Dqqdzk',1);
/*!40000 ALTER TABLE `oriented_gameiconswitchmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_gameslideovermodel`
--

DROP TABLE IF EXISTS `oriented_gameslideovermodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_gameslideovermodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `index` int(10) unsigned NOT NULL,
  `text` varchar(512) NOT NULL,
  `type` tinyint(1) NOT NULL,
  `imgLink` varchar(512) NOT NULL,
  `openType` tinyint(1) NOT NULL,
  `openUrl` varchar(20) NOT NULL,
  `isredon` tinyint(1) NOT NULL,
  `topath` varchar(512) NOT NULL,
  `bi_iconId` varchar(255) NOT NULL,
  `bi_landing_page` varchar(512) NOT NULL,
  `bi_landing_page_id` varchar(255) NOT NULL,
  `bi_educe_game` varchar(255) NOT NULL,
  `foreignkey_labelSlideOver_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oriented_gameslideov_foreignkey_labelSlid_1807f80c_fk_oriented_` (`foreignkey_labelSlideOver_id`),
  CONSTRAINT `oriented_gameslideov_foreignkey_labelSlid_1807f80c_fk_oriented_` FOREIGN KEY (`foreignkey_labelSlideOver_id`) REFERENCES `oriented_slideovermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_gameslideovermodel`
--

LOCK TABLES `oriented_gameslideovermodel` WRITE;
/*!40000 ALTER TABLE `oriented_gameslideovermodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `oriented_gameslideovermodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_gamestripmodel`
--

DROP TABLE IF EXISTS `oriented_gamestripmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_gamestripmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `index` int(10) unsigned NOT NULL,
  `wxAppId` varchar(20) NOT NULL,
  `imgLink` varchar(512) NOT NULL,
  `topath` varchar(512) NOT NULL,
  `isClickHide` tinyint(1) NOT NULL,
  `bi_iconId` varchar(255) NOT NULL,
  `bi_landing_page` varchar(512) NOT NULL,
  `bi_landing_page_id` varchar(255) NOT NULL,
  `bi_educe_game` varchar(255) NOT NULL,
  `foreignkey_strip_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oriented_gamestripmo_foreignkey_strip_id_84d6bc83_fk_oriented_` (`foreignkey_strip_id`),
  CONSTRAINT `oriented_gamestripmo_foreignkey_strip_id_84d6bc83_fk_oriented_` FOREIGN KEY (`foreignkey_strip_id`) REFERENCES `oriented_stripmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_gamestripmodel`
--

LOCK TABLES `oriented_gamestripmodel` WRITE;
/*!40000 ALTER TABLE `oriented_gamestripmodel` DISABLE KEYS */;
INSERT INTO `oriented_gamestripmodel` VALUES (1,0,'wxaa5c62c26ee49681','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/qiangshou.png','?from=3Dtsmg&togame=fkqs',0,'1512','https://sanxqn.nalrer.cn/tysanxiao/linkImages/1.png','728','fkqs',1),(2,3,'wx57f49f44206958e6','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/diaoyu.png','?from=3Dtsmg&togame=hldyds',0,'1515','https://sanxqn.nalrer.cn/tysanxiao/happyfishmaster/linkpage.jpg','729','hldyds',1),(3,9,'wx656cf75188e899bf','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/wudi.png','?from=3Dtsmg&togame=wgwd',0,'1521','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/wgwd.jpg','734','wgwd',1),(4,8,'wxd7062438a8b82506','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/fkft.png','?from=3Dtsmg&togame=fkft',0,'1523','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox6.jpg','736','fkft',1),(5,6,'wx30efe34580243475','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/tyxxbuyu.png','?from=3Dtsmg&togame=tyxxby',0,'1519','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/tyxxbuyu.jpg','737','tyxxby',1),(6,2,'wx7a2ecd52309f2466','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/russiaxccq.png','?from=3Dtsmg&togame=elsfkxccq',0,'1516','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox11.jpg','730','elsfkxccq',1),(7,1,'wxa3855d93c407a5b6','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/hlqsg.png','?from=3Dtsmg&togame=hlqsgds',0,'1517','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox9.jpg','731','hlqsgds',1),(8,5,'wx81df03575e1e351f','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/zumatq.png','?from=3Dtsmg&togame=zmtq',0,'1520','https://sanxqn.nalrer.cn/tysanxiao/linkImages/zuma.png','733','zmtq',1),(9,4,'wxde9361a6865997fc','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/3Dqq.png','?from=3Dtsmg&togame=3Dqqdzk',0,'1518','https://sanxqn.nalrer.cn/tysanxiao/fireball/linkimg_3D.png','732','3Dqqdzk',1),(10,7,'wxdb030d1934b15d67','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/szpp.png','?from=3Dtsmg&togame=szpp',0,'1522','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/szpp1.jpg','735','szpp',1),(11,2,'wx57f49f44206958e6','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/diaoyu.png','?from=zmtq&togame=hldyds',0,'836','https://sanxqn.nalrer.cn/tysanxiao/happyfishmaster/linkpage.jpg','200','hldyds',2),(12,3,'wxde9361a6865997fc','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/3Dqq.png','?from=zmtq&togame=3Dqqdzk',0,'914','https://sanxqn.nalrer.cn/tysanxiao/fireball/linkimg_3D.png','431','3Dqqdzk',2),(13,6,'wxbb777fbea1e15f52','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/newrussia2048.png','?from=zmtq&togame=newussia2048',0,'838','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/7.jpg','012','newussia2048',2),(14,1,'wx7a2ecd52309f2466','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/russiaxccq.png','?from=zmtq&togame=elsfkxccq',0,'1167','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/GameBox6.jpg','561','elsfkxccq',2),(15,8,'wx656cf75188e899bf','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/wudi.png','?from=zmtq&togame=wgwd',0,'841','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/wgwd.jpg','384','wgwd',2),(16,9,'wx4806f332084cae85','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/buyu.png','?from=zmtq&togame=tyby',0,'842','https://sanxqn.nalrer.cn/tysanxiao/linkImages/tyby.png','385','tyby',2),(17,4,'wxa3855d93c407a5b6','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/hlqsg.png','?from=zmtq&togame=hlqsgds',0,'1286','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/snipe_1.jpg','634','hlqsgds',2),(18,5,'wxdb030d1934b15d67','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/szpp.png','?from=zmtq&togame=szpp',0,'1573','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/szpp1.jpg','749','szpp',2),(19,7,'wx30b605819c95270b','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/zsl_1.png','?from=zmtq&togame=zhanshenlu',0,'1185','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/zsl_zuma.png','571','zhanshenlu',2),(20,0,'wxaa5c62c26ee49681','https://nslyqn.nalrer.cn/nsly/crazygun/growth/icon3/qiangshou.png','?from=zmtq&togame=fkqs',0,'357','https://nslyqn.nalrer.cn/nsly/crazygun/growth/luodiye/fkqsldy.png','099','fkqs',2);
/*!40000 ALTER TABLE `oriented_gamestripmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_iconswitchmodel`
--

DROP TABLE IF EXISTS `oriented_iconswitchmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_iconswitchmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `socket_url` int(10) unsigned NOT NULL,
  `switch` int(10) unsigned NOT NULL,
  `framesInterval` int(10) unsigned NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modifi_time` datetime(6) NOT NULL,
  `user` varchar(255) DEFAULT NULL,
  `online_modifi_time` datetime(6) DEFAULT NULL,
  `online_user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_iconswitchmodel`
--

LOCK TABLES `oriented_iconswitchmodel` WRITE;
/*!40000 ALTER TABLE `oriented_iconswitchmodel` DISABLE KEYS */;
INSERT INTO `oriented_iconswitchmodel` VALUES (1,20287,'wx234bfd171f00b4fc',1,1,5000,'2019-03-07 21:23:36.742176','2019-03-15 20:19:41.291037','cuijiuling','2019-03-15 20:19:56.630800','cuijiuling');
/*!40000 ALTER TABLE `oriented_iconswitchmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_positionmodel`
--

DROP TABLE IF EXISTS `oriented_positionmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_positionmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position_id` int(11) NOT NULL,
  `type` int(11) NOT NULL,
  `x` double NOT NULL,
  `y` double NOT NULL,
  `foreignkey_iconswitch_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `oriented_positionmod_foreignkey_iconswitc_17027bac_fk_oriented_` (`foreignkey_iconswitch_id`),
  CONSTRAINT `oriented_positionmod_foreignkey_iconswitc_17027bac_fk_oriented_` FOREIGN KEY (`foreignkey_iconswitch_id`) REFERENCES `oriented_iconswitchmodel` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_positionmodel`
--

LOCK TABLES `oriented_positionmodel` WRITE;
/*!40000 ALTER TABLE `oriented_positionmodel` DISABLE KEYS */;
INSERT INTO `oriented_positionmodel` VALUES (1,101,4,110.25,400,1),(2,102,2,55,550,1),(3,103,1,76,200,1);
/*!40000 ALTER TABLE `oriented_positionmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_slideovermodel`
--

DROP TABLE IF EXISTS `oriented_slideovermodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_slideovermodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `socket_url` int(10) unsigned NOT NULL,
  `switch` int(10) unsigned NOT NULL,
  `fromWhere` int(10) unsigned NOT NULL,
  `reddot` varchar(512) NOT NULL,
  `mask` varchar(512) NOT NULL,
  `viewAdCounts` int(10) unsigned NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modifi_time` datetime(6) NOT NULL,
  `user` varchar(255) DEFAULT NULL,
  `online_modifi_time` datetime(6) DEFAULT NULL,
  `online_user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_slideovermodel`
--

LOCK TABLES `oriented_slideovermodel` WRITE;
/*!40000 ALTER TABLE `oriented_slideovermodel` DISABLE KEYS */;
/*!40000 ALTER TABLE `oriented_slideovermodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oriented_stripmodel`
--

DROP TABLE IF EXISTS `oriented_stripmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oriented_stripmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `socket_url` int(10) unsigned NOT NULL,
  `label` varchar(512) NOT NULL,
  `bg` varchar(512) NOT NULL,
  `reddot` varchar(512) NOT NULL,
  `spacingX` int(10) unsigned NOT NULL,
  `iconWidth` int(10) unsigned NOT NULL,
  `iconHeight` int(10) unsigned NOT NULL,
  `switch` int(10) unsigned NOT NULL,
  `viewAdCounts` int(10) unsigned NOT NULL,
  `framesInterval` int(10) unsigned NOT NULL,
  `create_time` datetime(6) NOT NULL,
  `modifi_time` datetime(6) NOT NULL,
  `user` varchar(255) DEFAULT NULL,
  `online_modifi_time` datetime(6) DEFAULT NULL,
  `online_user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oriented_stripmodel`
--

LOCK TABLES `oriented_stripmodel` WRITE;
/*!40000 ALTER TABLE `oriented_stripmodel` DISABLE KEYS */;
INSERT INTO `oriented_stripmodel` VALUES (1,20287,'wx234bfd171f00b4fc',1,'https://sanxqn.nalrer.cn/tysanxiao/box/adImg/sxbg0.png','https://sanxqn.nalrer.cn/tysanxiao/box/adImg/adbg.png','https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/reddot.png',10,117,142,1,5,20000,'2019-03-07 21:24:19.919622','2019-03-15 20:52:46.106320','cuijiuling','2019-03-15 20:52:58.807572','cuijiuling'),(2,20037,'wx81df03575e1e351f',1,'https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/label.png','https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/adRes.png','https://sanxqn.nalrer.cn/tysanxiao/test/LikeConfigRes/reddot.png',10,117,142,1,5,50,'2019-03-15 11:58:39.338853','2019-03-15 11:58:39.339002','import',NULL,NULL);
/*!40000 ALTER TABLE `oriented_stripmodel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upload_uploadmodel`
--

DROP TABLE IF EXISTS `upload_uploadmodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upload_uploadmodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(10) unsigned NOT NULL,
  `socket_url` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `oriented_type` varchar(255) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `file` varchar(100) NOT NULL,
  `user` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upload_uploadmodel`
--

LOCK TABLES `upload_uploadmodel` WRITE;
/*!40000 ALTER TABLE `upload_uploadmodel` DISABLE KEYS */;
INSERT INTO `upload_uploadmodel` VALUES (1,20037,1,'wx81df03575e1e351f','1',1,'zm_bt_config5_2019-03-15_0867008e46.json','cuijiuling');
/*!40000 ALTER TABLE `upload_uploadmodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-02 23:59:02
