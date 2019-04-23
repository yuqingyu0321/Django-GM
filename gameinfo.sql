-- MySQL dump 10.13  Distrib 5.7.25, for macos10.14 (x86_64)
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
-- Table structure for table `gameInfo_gameinfomodel`
--

DROP TABLE IF EXISTS `gameInfo_gameinfomodel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gameInfo_gameinfomodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `game_id` int(10) unsigned NOT NULL,
  `name` varchar(255) NOT NULL,
  `wxAppid` varchar(21) NOT NULL,
  `socket_url` int(10) unsigned NOT NULL,
  `inner_game` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gameInfo_gameinfomodel`
--

LOCK TABLES `gameInfo_gameinfomodel` WRITE;
/*!40000 ALTER TABLE `gameInfo_gameinfomodel` DISABLE KEYS */;
INSERT INTO `gameInfo_gameinfomodel` VALUES (1,309,'旅行小西瓜','wx81319a080b7919e2',1,1),(2,20037,'祖玛弹球','wx81df03575e1e351f',1,1),(3,106,'疯狂枪手','wxaa5c62c26ee49681',0,1),(4,6,'富豪斗地主','wxbfebdafc2fc60b54',0,1),(5,301,'新俄罗斯2048','wxbb777fbea1e15f52',1,1),(6,20081,'十字消消消','wxb1d95fb6ebaf04eb',1,1),(7,20100,'2048合并','wx9f3847ace08e2ef0',1,1),(8,20111,'欢乐钓鱼大师','wx57f49f44206958e6',1,1),(9,302,'经典俄罗斯2048','wxf1e6cc8e12d25d1f',1,1),(10,110,'天天狙击','wx6a9fc3d2c62410d8',0,1),(11,115,'双枪王者','wx824d94ce511885ad',0,1),(12,108,'数字消消乐2','wxb082d51f37021fac',0,1),(13,20180,'欢乐挖矿大师','wxe28531ea9f8164dc',1,1),(14,20178,'碰撞球球','wx3e051a032d2386e9',1,1),(15,6,'单机斗地主','wxc1b648fc2fbc7ce8',1,1),(16,20136,'球球大消除','wx160e205dd45116c4',1,1),(17,20205,'3D球球打砖块','wxde9361a6865997fc',1,1),(18,20232,'疯狂斧头','wxd7062438a8b82506',1,1),(19,127,'合到8','wx352edabae2ef7a26',0,1),(20,125,'合并三国','wxca71cd422b7fa67c',0,1),(21,20241,'欢乐切水果大师','wxa3855d93c407a5b6',1,1),(22,20288,'欢乐涂色大师','wx950f5176e1d4ea9c',1,1),(23,128,'飞刀对战','wx2ff277bf28f5b970',0,1),(24,20287,'3D涂色迷宫','wx234bfd171f00b4fc',1,1),(25,20299,'3D割草大师','wxb7cb93eb49278934',1,1),(26,20235,'俄罗斯方块消除传奇','wx7a2ecd52309f2466',1,1),(27,0,'天天游乐场','wx1668490543c6bae9',9999,0),(28,0,'途游斗地主','wx785e80cff6120de5',9999,0),(29,0,'传奇来了','wx79ade44c39cefc7f',9999,0),(30,0,'世界争霸','wxe11c116fc919cca1',9999,0),(31,0,'龙城战歌','wx533d91264e8c999c',9999,0),(32,0,'俄罗斯方块拼图','wx45e02fc734c7b568',9999,0),(33,0,'欢乐途游麻将','wxe46bd15fcbb4f829',9999,0),(34,0,'途游休闲捕鱼','wx30efe34580243475',9999,0),(35,0,'途游四川麻将','wxa9b801abd43333d9',9999,0),(36,0,'途游捕鱼','wx4806f332084cae85',9999,0),(37,0,'3D战警','wx7cc3368d8ea0ed18',9999,0),(38,0,'西部射杀','wx85e9ff1a243bd54c',9999,0),(39,0,'王国无敌','wx656cf75188e899bf',9999,0),(40,0,'搭木板','wxe20385ecec37a61d',9999,0),(41,0,'欢乐加1','wxd9dac6412c7dab7b',9999,0),(42,0,'数字三消','wx9bb2c795e0a6cc26',9999,0),(43,0,'2048六角消除','wxb92d4d650d51eda8',9999,0),(44,0,'星星萌翻天','wx9b028af0bedc1ea7',9999,0),(45,0,'玩爆2048','wx38ba6e1a02228283',9999,0),(46,0,'枪手来了','wx760b441f8a68d7c6',9999,0),(47,0,'球球飞车','wx148b43768fd2f0c8',9999,0),(48,0,'大海王','wx720172c3c7b560c5',9999,0),(49,0,'战神录','wx30b605819c95270b',9999,0),(50,0,'沙城战神','wx7243aa518129131d',9999,0),(51,0,'左右冲鸭','wx6ae9fecf13de0423',9999,0),(52,0,'挪车大师','wxd82849dc23eb4ac0',9999,0),(53,0,'数字泡泡','wxdb030d1934b15d67',9999,0),(54,0,'途游游戏','wx4b05395b61fd2aaf',9999,0);
/*!40000 ALTER TABLE `gameInfo_gameinfomodel` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-23 17:00:18
