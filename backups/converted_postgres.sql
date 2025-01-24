-- MySQL dump 10.13  Distrib 8.0.40, for Linux (x86_64)
--
-- Host: localhost    Database: ttranking
-- ------------------------------------------------------
-- Server version	8.0.40-0ubuntu0.24.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table "auth_group"
--

DROP TABLE IF EXISTS "auth_group";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_group" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(150) NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "name" ("name")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_group"
--


/*!40000 ALTER TABLE "auth_group" DISABLE KEYS */;
/*!40000 ALTER TABLE "auth_group" ENABLE KEYS */;
UN

--
-- Table structure for table "auth_group_permissions"
--

DROP TABLE IF EXISTS "auth_group_permissions";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_group_permissions" (
  "id" bigSERIAL PRIMARY KEY,
  "group_id" int NOT NULL,
  "permission_id" int NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ("group_id","permission_id"),
  KEY "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" ("permission_id"),
  CONSTRAINT "auth_group_permissio_permission_id_84c5c92e_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id"),
  CONSTRAINT "auth_group_permissions_group_id_b120cbf9_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_group_permissions"
--


/*!40000 ALTER TABLE "auth_group_permissions" DISABLE KEYS */;
/*!40000 ALTER TABLE "auth_group_permissions" ENABLE KEYS */;
UN

--
-- Table structure for table "auth_permission"
--

DROP TABLE IF EXISTS "auth_permission";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_permission" (
  "id" SERIAL PRIMARY KEY,
  "name" varchar(255) NOT NULL,
  "content_type_id" int NOT NULL,
  "codename" varchar(100) NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "auth_permission_content_type_id_codename_01ab375a_uniq" ("content_type_id","codename"),
  CONSTRAINT "auth_permission_content_type_id_2f476e4b_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_permission"
--


/*!40000 ALTER TABLE "auth_permission" DISABLE KEYS */;
INSERT INTO "auth_permission" VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add match stats',7,'add_matchstats'),(26,'Can change match stats',7,'change_matchstats'),(27,'Can delete match stats',7,'delete_matchstats'),(28,'Can view match stats',7,'view_matchstats'),(29,'Can add doubles match',8,'add_doublesmatch'),(30,'Can change doubles match',8,'change_doublesmatch'),(31,'Can delete doubles match',8,'delete_doublesmatch'),(32,'Can view doubles match',8,'view_doublesmatch'),(33,'Can add singles match',9,'add_singlesmatch'),(34,'Can change singles match',9,'change_singlesmatch'),(35,'Can delete singles match',9,'delete_singlesmatch'),(36,'Can view singles match',9,'view_singlesmatch'),(37,'Can add player',10,'add_player'),(38,'Can change player',10,'change_player'),(39,'Can delete player',10,'delete_player'),(40,'Can view player',10,'view_player'),(41,'Can add Token',11,'add_token'),(42,'Can change Token',11,'change_token'),(43,'Can delete Token',11,'delete_token'),(44,'Can view Token',11,'view_token'),(45,'Can add Token',12,'add_tokenproxy'),(46,'Can change Token',12,'change_tokenproxy'),(47,'Can delete Token',12,'delete_tokenproxy'),(48,'Can view Token',12,'view_tokenproxy');
/*!40000 ALTER TABLE "auth_permission" ENABLE KEYS */;
UN

--
-- Table structure for table "auth_user"
--

DROP TABLE IF EXISTS "auth_user";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_user" (
  "id" SERIAL PRIMARY KEY,
  "password" varchar(128) NOT NULL,
  "last_login" datetime(6) DEFAULT NULL,
  "is_superuser" tinyint(1) NOT NULL,
  "username" varchar(150) NOT NULL,
  "first_name" varchar(150) NOT NULL,
  "last_name" varchar(150) NOT NULL,
  "email" varchar(254) NOT NULL,
  "is_staff" tinyint(1) NOT NULL,
  "is_active" tinyint(1) NOT NULL,
  "date_joined" datetime(6) NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "username" ("username")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_user"
--


/*!40000 ALTER TABLE "auth_user" DISABLE KEYS */;
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$720000$RcLJW6vgkkHpGdTV5AHVPD$OfNvIvoeYxxNZxQgUwqypV6JxtiHt30e/B1IkS7iqRw=','2024-12-12 18:19:49.013066',1,'juan','','','sobalvarrog.juans@gmail.com',1,1,'2024-08-06 02:48:09.252871'),(2,'pbkdf2_sha256$720000$zRl7uaN7wufT2BjFdBuQ2G$tSGSiZK062HjojLGt430Ey0DjSHf7fFk0HY9PwIbLSs=','2024-11-15 02:09:54.096769',0,'alfredo','','','',1,1,'2024-08-06 02:49:23.000000'),(3,'pbkdf2_sha256$720000$43RG9OFrRTP9HrasGXxqP0$x7Cucu+IOriLjkR95vr5eWgBobgU+2k94pG4AWP11js=','2024-08-29 14:35:40.717664',0,'aarock','Aarón','Cisneros','',1,1,'2024-08-21 20:49:13.000000'),(4,'pbkdf2_sha256$720000$vRcGOjchpPR26tZtgJT41V$KVe64xWnL7RfTNqGzd+mQ2qlbO34QRJMUaqeDpRq5P8=','2024-09-16 18:38:17.463507',1,'heyner','','','',1,1,'2024-09-16 18:37:24.021540');
/*!40000 ALTER TABLE "auth_user" ENABLE KEYS */;
UN

--
-- Table structure for table "auth_user_groups"
--

DROP TABLE IF EXISTS "auth_user_groups";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_user_groups" (
  "id" bigSERIAL PRIMARY KEY,
  "user_id" int NOT NULL,
  "group_id" int NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "auth_user_groups_user_id_group_id_94350c0c_uniq" ("user_id","group_id"),
  KEY "auth_user_groups_group_id_97559544_fk_auth_group_id" ("group_id"),
  CONSTRAINT "auth_user_groups_group_id_97559544_fk_auth_group_id" FOREIGN KEY ("group_id") REFERENCES "auth_group" ("id"),
  CONSTRAINT "auth_user_groups_user_id_6a12ed8b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_user_groups"
--


/*!40000 ALTER TABLE "auth_user_groups" DISABLE KEYS */;
/*!40000 ALTER TABLE "auth_user_groups" ENABLE KEYS */;
UN

--
-- Table structure for table "auth_user_user_permissions"
--

DROP TABLE IF EXISTS "auth_user_user_permissions";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "auth_user_user_permissions" (
  "id" bigSERIAL PRIMARY KEY,
  "user_id" int NOT NULL,
  "permission_id" int NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ("user_id","permission_id"),
  KEY "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" ("permission_id"),
  CONSTRAINT "auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm" FOREIGN KEY ("permission_id") REFERENCES "auth_permission" ("id"),
  CONSTRAINT "auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "auth_user_user_permissions"
--


/*!40000 ALTER TABLE "auth_user_user_permissions" DISABLE KEYS */;
/*!40000 ALTER TABLE "auth_user_user_permissions" ENABLE KEYS */;
UN

--
-- Table structure for table "authtoken_token"
--

DROP TABLE IF EXISTS "authtoken_token";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "authtoken_token" (
  "key" varchar(40) NOT NULL,
  "created" datetime(6) NOT NULL,
  "user_id" int NOT NULL,
  PRIMARY KEY ("key"),
  UNIQUE KEY "user_id" ("user_id"),
  CONSTRAINT "authtoken_token_user_id_35299eff_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "authtoken_token"
--


/*!40000 ALTER TABLE "authtoken_token" DISABLE KEYS */;
INSERT INTO "authtoken_token" VALUES ('643953eb716c93adcb5d15e0453b81fa151e3f10','2024-09-16 18:37:24.629493',4),('b1d20e0fba75e45255b53af526ba1ea3810182c1','2024-08-21 20:49:13.947563',3);
/*!40000 ALTER TABLE "authtoken_token" ENABLE KEYS */;
UN

--
-- Table structure for table "django_admin_log"
--

DROP TABLE IF EXISTS "django_admin_log";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "django_admin_log" (
  "id" SERIAL PRIMARY KEY,
  "action_time" datetime(6) NOT NULL,
  "object_id" TEXT,
  "object_repr" varchar(200) NOT NULL,
  "action_flag" smallint unsigned NOT NULL,
  "change_message" TEXT NOT NULL,
  "content_type_id" int DEFAULT NULL,
  "user_id" int NOT NULL,
  PRIMARY KEY ("id"),
  KEY "django_admin_log_content_type_id_c4bce8eb_fk_django_co" ("content_type_id"),
  KEY "django_admin_log_user_id_c564eba6_fk_auth_user_id" ("user_id"),
  CONSTRAINT "django_admin_log_content_type_id_c4bce8eb_fk_django_co" FOREIGN KEY ("content_type_id") REFERENCES "django_content_type" ("id"),
  CONSTRAINT "django_admin_log_user_id_c564eba6_fk_auth_user_id" FOREIGN KEY ("user_id") REFERENCES "auth_user" ("id"),
  CONSTRAINT "django_admin_log_chk_1" CHECK (("action_flag" >= 0))
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "django_admin_log"
--


/*!40000 ALTER TABLE "django_admin_log" DISABLE KEYS */;
INSERT INTO "django_admin_log" VALUES (1,'2024-08-06 02:49:23.651153','2','alfredo',1,'[{\"added\": {}}]',4,1),(2,'2024-08-06 02:49:57.057489','2','alfredo',2,'[{\"changed\": {\"fields\": [\"Staff status\"]}}]',4,1),(3,'2024-08-21 20:49:13.949455','3','Aarock',1,'[{\"added\": {}}]',4,1),(4,'2024-08-21 20:49:35.719070','3','Aarock',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\", \"Staff status\"]}}]',4,1),(5,'2024-08-21 20:49:47.079808','3','aarock',2,'[{\"changed\": {\"fields\": [\"Username\"]}}]',4,1),(6,'2024-08-21 20:59:12.908372','3','aarock',2,'[{\"changed\": {\"fields\": [\"password\"]}}]',4,1);
/*!40000 ALTER TABLE "django_admin_log" ENABLE KEYS */;
UN

--
-- Table structure for table "django_content_type"
--

DROP TABLE IF EXISTS "django_content_type";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "django_content_type" (
  "id" SERIAL PRIMARY KEY,
  "app_label" varchar(100) NOT NULL,
  "model" varchar(100) NOT NULL,
  PRIMARY KEY ("id"),
  UNIQUE KEY "django_content_type_app_label_model_76bd3d3b_uniq" ("app_label","model")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "django_content_type"
--


/*!40000 ALTER TABLE "django_content_type" DISABLE KEYS */;
INSERT INTO "django_content_type" VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(11,'authtoken','token'),(12,'authtoken','tokenproxy'),(5,'contenttypes','contenttype'),(8,'matches','doublesmatch'),(7,'matches','matchstats'),(9,'matches','singlesmatch'),(10,'players','player'),(6,'sessions','session');
/*!40000 ALTER TABLE "django_content_type" ENABLE KEYS */;
UN

--
-- Table structure for table "django_migrations"
--

DROP TABLE IF EXISTS "django_migrations";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "django_migrations" (
  "id" bigSERIAL PRIMARY KEY,
  "app" varchar(255) NOT NULL,
  "name" varchar(255) NOT NULL,
  "applied" datetime(6) NOT NULL,
  PRIMARY KEY ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "django_migrations"
--


/*!40000 ALTER TABLE "django_migrations" DISABLE KEYS */;
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2024-08-06 02:04:26.875996'),(2,'auth','0001_initial','2024-08-06 02:04:28.016770'),(3,'admin','0001_initial','2024-08-06 02:04:28.307984'),(4,'admin','0002_logentry_remove_auto_add','2024-08-06 02:04:28.322659'),(5,'admin','0003_logentry_add_action_flag_choices','2024-08-06 02:04:28.336169'),(6,'contenttypes','0002_remove_content_type_name','2024-08-06 02:04:28.473753'),(7,'auth','0002_alter_permission_name_max_length','2024-08-06 02:04:28.601671'),(8,'auth','0003_alter_user_email_max_length','2024-08-06 02:04:28.637921'),(9,'auth','0004_alter_user_username_opts','2024-08-06 02:04:28.651475'),(10,'auth','0005_alter_user_last_login_null','2024-08-06 02:04:28.751558'),(11,'auth','0006_require_contenttypes_0002','2024-08-06 02:04:28.757315'),(12,'auth','0007_alter_validators_add_error_messages','2024-08-06 02:04:28.770773'),(13,'auth','0008_alter_user_username_max_length','2024-08-06 02:04:28.884555'),(14,'auth','0009_alter_user_last_name_max_length','2024-08-06 02:04:28.997363'),(15,'auth','0010_alter_group_name_max_length','2024-08-06 02:04:29.028496'),(16,'auth','0011_update_proxy_permissions','2024-08-06 02:04:29.041860'),(17,'auth','0012_alter_user_first_name_max_length','2024-08-06 02:04:29.153586'),(18,'players','0001_initial','2024-08-06 02:04:29.199639'),(19,'matches','0001_initial','2024-08-06 02:04:29.731466'),(20,'matches','0002_doublesmatch_matchstats_doubles_match_singlesmatch_and_more','2024-08-06 02:04:31.052814'),(21,'matches','0003_remove_doublesmatch_score_remove_singlesmatch_score_and_more','2024-08-06 02:04:31.371515'),(22,'matches','0004_alter_doublesmatch_winner_team','2024-08-06 02:04:31.382403'),(23,'players','0002_alter_player_nationality_alter_player_ranking','2024-08-06 02:04:31.492464'),(24,'players','0003_alter_player_date_of_birth_alter_player_ranking','2024-08-06 02:04:31.591447'),(25,'players','0004_player_alias_alter_player_photo','2024-08-06 02:04:31.639553'),(26,'players','0005_alter_player_photo','2024-08-06 02:04:31.649686'),(27,'players','0006_player_gender','2024-08-06 02:04:31.695939'),(28,'players','0007_alter_player_gender','2024-08-06 02:04:31.841109'),(29,'players','0008_player_created_at_player_updated_at_and_more','2024-08-06 02:04:32.101788'),(30,'players','0009_remove_player_updated_by','2024-08-06 02:04:32.251879'),(31,'sessions','0001_initial','2024-08-06 02:04:32.325012'),(32,'authtoken','0001_initial','2024-08-10 20:03:57.522714'),(33,'authtoken','0002_auto_20160226_1747','2024-08-10 20:03:57.558157'),(34,'authtoken','0003_tokenproxy','2024-08-10 20:03:57.565222'),(35,'authtoken','0004_alter_tokenproxy_options','2024-08-10 20:03:57.574722'),(36,'matches','0005_delete_matchstats','2024-08-10 20:03:57.613574'),(37,'players','0010_alter_player_nationality','2024-08-10 20:03:57.624697'),(38,'players','0011_player_matches_played','2024-08-10 20:03:57.691234');
/*!40000 ALTER TABLE "django_migrations" ENABLE KEYS */;
UN

--
-- Table structure for table "django_session"
--

DROP TABLE IF EXISTS "django_session";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "django_session" (
  "session_key" varchar(40) NOT NULL,
  "session_data" TEXT NOT NULL,
  "expire_date" datetime(6) NOT NULL,
  PRIMARY KEY ("session_key"),
  KEY "django_session_expire_date_a5c62663" ("expire_date")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "django_session"
--


/*!40000 ALTER TABLE "django_session" DISABLE KEYS */;
INSERT INTO "django_session" VALUES ('17xm1efkffvp054ikiabq0qu5i5o1vjv','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tL5P9:rzojz5_rP9yFZtuC4t40hmPOmYwueKrSFmV-YLog79I','2024-12-10 19:26:19.841833'),('1cefysjgs4dyk8xsy9euk9ntscicl302','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tLoO8:Melicrk9vS_hy8dq_ZZzEXX1T81tIjPnwIMNTr2kBF8','2024-12-12 19:28:16.819481'),('2c8nofu2flad31k8ap50xp7zrp76v8xr','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tDpZG:9bnFwsAuKk-NhXooMWyTGjG8k0UIXN-epprORQa1x4w','2024-11-20 19:06:46.433888'),('2ma5m4ayz3cevrz7fzwyudbxivntaqsm','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1sct1j:zYl2YjLvlgXSpgQsW5NZNp4e17Z9X15bJlokIAZIH64','2024-08-10 21:19:27.203488'),('2vyarr7mm2epinpcmmei6hv9eq5wyybg','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tDpYn:X66UzyrwU-sluMlHAQ6voOtnsgAfYk2DXEYPOZuPYoA','2024-11-20 19:06:17.219468'),('41fuenyou4ybaym99dlz3b7dfylbf6z3','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t97jf:e7HG5cI3r10LgqPW8fUx2c2uXC4Xq5KBSeVo1BfK_Oc','2024-11-07 19:30:03.198238'),('4g2d7ak8za76gc5cc79mhxll0ydh34aw','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t3gXD:uusOapCP7Xtc7S1vUQJvl5DunV3opVBXWZoDU7eNtac','2024-10-23 19:26:43.739232'),('5nbxqh8lq75969ptu44kgu2z7qyaeaom','e30:1sf07F:x56_6de0hluvmESk0IFTBiI0YEGLWlBsatRx1eG8E2E','2024-08-16 17:17:53.922222'),('7fz06joxdx8dwbz10wys8eu2uepp51n0','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1sdhXP:2ROUMIx_fYxPzvSof1tMtF0uweaDQ93Hutonae3e1Fk','2024-08-13 03:15:31.371343'),('7yreavak8rrw7vxrnwvfgyd9exhjmai8','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1spBYn:5rnBCDxK96W9O8884KoVns7V6AXOyT5oOfNkPr7EnZw','2024-09-13 19:32:25.200666'),('8v29fd1fw4eyq0z5olml4gueak8lvmd2','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1soSXN:hd6FzMaz7JZ6PqaAi2YuDVZEXmTJyZJZWX0qy28CKRQ','2024-09-11 19:27:57.969160'),('9h2tc3p2e0n2wnojnikzw9imghlz0qlj','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tIudy:8gJQjlFTXK52f1MaO-uOB6hRAOJuhPJsSWqIVGrAmDY','2024-12-04 19:32:38.247746'),('a0zs91gke7brha66pfqe36mmcgycujal','e30:1sez26:hqmDwwplXqSvhht_9Fm_JaOKTYaCkv-XcC-Hh_7bj7s','2024-08-16 16:08:30.457052'),('arkximmw95yg5vfnszib53ubpjmuxcq5','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tDpvx:eVdcXxTkEi3Hu00DAdW7VqJPVqYtyTPi2IGhsgzL4Hc','2024-11-20 19:30:13.968060'),('c1mf4d9xinwkr8r6tzv5fys8annh2pbq','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1so63N:qzYQMAynyadtFFBuSwtKhaM_9vZ8_FsqVEBODoFPz6Y','2024-09-10 19:27:29.491040'),('di6r7sahof9xf4ynewhgu5ihfnvhhrmz','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1srM3N:SZPCbDukXPJKo9N_yMK1muiQCjhcOUQhSJRPoQzp7j8','2024-09-19 19:08:57.796685'),('dv9z80o8pekwkb257obxl25d2uj21dv0','e30:1seidr:EsJ8dLZmW6XwNyO1RTGiSGhF91mLCQPOu-_14qPKRDs','2024-08-15 22:38:23.352943'),('f5dea12btx1r5hk3naeadyra6886b60l','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tC1Vq:DAkN-i3WgEtyGnK9gCr7XjUSV8vtdQ0QF_r7AoYFQzY','2024-11-15 19:27:46.022015'),('g7ue56vxafhn6615p9oj1n9hw5bxofgx','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t434W:E6mzzxAjKXSGBd_xs2AnjxJhnoMBBCzxupDu865OSFc','2024-10-24 19:30:36.625271'),('gc1q9yks6l6qtyykep5hpekjednlocx7','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tIY4K:fCQNUsfenfDMzQQIL5i-FCpJ5e2bIlvROJHept3YuiA','2024-12-03 19:26:20.039646'),('hs1hgrt2jyo5otqeok2mhvtfypd1qupx','.eJxVjEEOwiAQRe_C2pCWAQGX7nsGMgyDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-t4j04LqDdMd6a5JaXZc5yl2RB-1yaomf18P9OyjYy7e2BDHl7AhhNKSNMQ601YwKLLD1lnyEIakMrM6OfeYxGSDwMTLQkMX7A-nbOEI:1tBl6x:L3-p_iQMQEjVd0eIZJE1oeikKk_H2_BLAWZJRS4x2kA','2024-11-15 01:56:59.307378'),('ip2fb05ijl4ouql2u74m44n45ffxzq3w','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t1ruJ:LvvFnb_I7NKqZ6JrjVLdVxSEf3Rab6tZankCSIrNndk','2024-10-18 19:11:03.457316'),('jdw2leamldq9ot7rbnb9d16n2r0o3x46','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tC7DY:C6JolYPoX6-5WZfB7vNu6RE2glx_hc9iGPm4CJXcy30','2024-11-16 01:33:16.203035'),('l2yutse2sdxe32zuqg8rj6a286moj515','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t4PSO:UjLwGQawRHXAGjgVpbdRtO3orG1yWbhHgKjRROF_1Nw','2024-10-25 19:24:44.662046'),('n25ysxtrs2yc8bhe9qvslthoil7ocuwx','.eJxVjEEOwiAQRe_C2pAZQCgu3fcMhGEGWzVtUtqV8e7apAvd_vfef6mUt3VIW5MljawuyqnT70a5PGTaAd_zdJt1mad1GUnvij5o0_3M8rwe7t_BkNvwrU0k75Gwq-AQIAAAFyzRoUHHQuLw3EUO1lIxFiSYSiGw6cSzD9Wq9we2VjcE:1sqGck:bF6oF5t-D1rs4uIcq3kND2vJfo4A2lPvfwaCmsehSpE','2024-09-16 19:08:58.400008'),('n6e52s9bg21piusgh51085472ppeue33','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1seh5R:FY6Kn-TLswmiwbuzycgZX7bnSGty67V6mU3vnReFFbw','2024-08-15 20:58:45.735054'),('o6444mmvqmqrkkbhmxf33ujxqsnzvifz','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1sd35R:wYLMO9hzx2kEuB7dMPIMGk-Y0W7JR3IOxOmf7qpmNUM','2024-08-11 08:03:57.761149'),('ojxl6s2pac8rv3z6gnfylddmf2mg6unz','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tGNDt:Bf1HbbFzy0Yre1BIysuxY8j0CJE09s6tA9mzZ2xvxcs','2024-11-27 19:27:13.873670'),('p04244bxssdxcnym0hq50xef4h732ukg','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1sbAov:l0mGQkHf7FWDhR_GF2YnAFBQUYujC59yCIPrXh7IqXU','2024-08-20 03:25:09.642335'),('p2ex79l717k6igxi20owbpplkbze0pca','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tBNSH:731wNM6M7hMbbFrviHer_k-FBZWkQ9hz8iQuzOQuYfs','2024-11-14 00:41:25.423554'),('qhtvzbh3iootiajx4wdzdjrn9v3g2ua5','e30:1scuYt:fb1V5JdyoN0ivWA7MJcyUPO5KglVx6MxqBKspo7mBhQ','2024-08-10 22:57:47.886493'),('r8rxcsyyyud3ttstujdgebeu7x0nik7q','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1sczYk:8TbUwDujxxx7eIW0SAYfQGOCAVre__jRYnc3lJKGY8w','2024-08-11 04:17:58.688390'),('sdob3g624kc4e05yx87moa8zd7drcvxk','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t19GQ:5wSI7VM5t1qKT4g0xkhRk15jRP6k6YNudZ5LHw004ic','2024-10-16 19:30:54.365102'),('srbq2p86qzej8xnw9v6iwc03plsctjye','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tBf3M:mF20eo9zQwsFJ1wBHP1ql-1mvbUSeRTzMlMG9HZPmW4','2024-11-14 19:28:52.259273'),('thrd7r14yaqyp8dhpq0zslka0s1hkxcx','.eJxVjEEOwiAQRe_C2pCWAQGX7nsGMgyDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-t4j04LqDdMd6a5JaXZc5yl2RB-1yaomf18P9OyjYy7e2BDHl7AhhNKSNMQ601YwKLLD1lnyEIakMrM6OfeYxGSDwMTLQkMX7A-nbOEI:1sgPfa:w6jLyKF3LFUluyZMkm0CM6DEdVTggGI5OdUsGK8QPkA','2024-08-20 14:47:10.663081'),('to116cmy8os626e0ck9szskgt0tmaolj','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1tJdVc:HQgMXHk98DMhZ42ZZi2uv21WPbSwKfx4GWjfsTNg8oU','2024-12-06 19:27:00.594007'),('u8izkocz6nr8ymo8j80q8o0ghwsja2qx','.eJxVjEEOwiAQRe_C2pCWAQGX7nsGMgyDVA0kpV0Z765NutDtf-_9lwi4rSVsnZcwJ3ERSpx-t4j04LqDdMd6a5JaXZc5yl2RB-1yaomf18P9OyjYy7e2BDHl7AhhNKSNMQ601YwKLLD1lnyEIakMrM6OfeYxGSDwMTLQkMX7A-nbOEI:1sdxHd:6X5AnEkw-VHCGceUBJmwbteshAbeyc61P_RIglOv2Yg','2024-08-13 20:04:17.720799'),('xec3q1q5twf8l1evbqdjwv7gff5d4kyz','e30:1sekrS:_PQSBiixU0arf3wApAYNTFeojAUw42wxJGsc0tMnz2c','2024-08-16 01:00:34.366211'),('yy1eun6p7cmzxpirw5yt3foqzhzalyun','.eJxVjEEOgjAQRe_StWk6FTrUpXvOQGY6U4saSCisjHdXEha6_e-9_zIDbWsZtqrLMIq5GDCn340pPXTagdxpus02zdO6jGx3xR602n4WfV4P9--gUC3fuo0JKDcxdOw9eg-B0bXQNoqC6lzUxBK0Ic4OGYNARtIzC2iXPYB5fwDTuTf7:1t8O6J:U7iuRFT6N6WagiwfKtDZoHFuJsZW1L63q5KehO8qkho','2024-11-05 18:46:23.302488');
/*!40000 ALTER TABLE "django_session" ENABLE KEYS */;
UN

--
-- Table structure for table "matches_doublesmatch"
--

DROP TABLE IF EXISTS "matches_doublesmatch";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "matches_doublesmatch" (
  "id" bigSERIAL PRIMARY KEY,
  "date" datetime(6) NOT NULL,
  "winner_team" varchar(10) DEFAULT NULL,
  "team1_player1_id" bigint NOT NULL,
  "team1_player2_id" bigint NOT NULL,
  "team2_player1_id" bigint NOT NULL,
  "team2_player2_id" bigint NOT NULL,
  "team1_score" int NOT NULL,
  "team2_score" int NOT NULL,
  PRIMARY KEY ("id"),
  KEY "matches_doublesmatch_team1_player1_id_e9cebfce_fk_players_p" ("team1_player1_id"),
  KEY "matches_doublesmatch_team1_player2_id_ab14e756_fk_players_p" ("team1_player2_id"),
  KEY "matches_doublesmatch_team2_player1_id_3601d9f9_fk_players_p" ("team2_player1_id"),
  KEY "matches_doublesmatch_team2_player2_id_61573f4e_fk_players_p" ("team2_player2_id"),
  CONSTRAINT "matches_doublesmatch_team1_player1_id_e9cebfce_fk_players_p" FOREIGN KEY ("team1_player1_id") REFERENCES "players_player" ("id"),
  CONSTRAINT "matches_doublesmatch_team1_player2_id_ab14e756_fk_players_p" FOREIGN KEY ("team1_player2_id") REFERENCES "players_player" ("id"),
  CONSTRAINT "matches_doublesmatch_team2_player1_id_3601d9f9_fk_players_p" FOREIGN KEY ("team2_player1_id") REFERENCES "players_player" ("id"),
  CONSTRAINT "matches_doublesmatch_team2_player2_id_61573f4e_fk_players_p" FOREIGN KEY ("team2_player2_id") REFERENCES "players_player" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "matches_doublesmatch"
--


/*!40000 ALTER TABLE "matches_doublesmatch" DISABLE KEYS */;
INSERT INTO "matches_doublesmatch" VALUES (1,'2024-08-06 06:29:00.000000','Team 1',12,9,1,7,13,11),(2,'2024-08-06 06:32:00.000000','Team 1',12,9,18,1,11,0),(3,'2024-08-06 06:33:00.000000','Team 1',12,9,5,8,11,6),(4,'2024-08-06 06:41:00.000000','Team 1',12,9,1,18,11,9),(5,'2024-08-06 06:44:00.000000','Team 1',12,9,8,5,11,7),(6,'2024-08-06 06:45:00.000000','Team 2',17,14,1,7,6,11),(7,'2024-08-06 06:49:00.000000','Team 1',12,9,17,14,11,1),(8,'2024-08-06 06:51:00.000000','Team 1',12,9,7,1,11,8),(9,'2024-08-06 06:52:00.000000','Team 1',12,9,14,17,11,0),(10,'2024-08-06 06:53:00.000000','Team 1',12,9,1,18,11,8),(11,'2024-08-06 06:57:00.000000','Team 1',12,9,5,8,11,5),(12,'2024-08-06 06:58:00.000000','Team 1',7,1,20,19,11,5),(13,'2024-08-06 07:00:00.000000','Team 1',9,12,19,20,11,1),(14,'2024-08-06 07:01:00.000000','Team 1',12,9,20,19,11,0),(15,'2024-08-06 07:06:00.000000','Team 1',9,12,19,20,11,5),(16,'2024-08-06 14:57:00.000000','Team 1',5,15,18,8,11,5),(17,'2024-08-06 15:01:00.000000','Team 1',5,15,11,21,11,4),(18,'2024-08-06 15:01:00.000000','Team 2',5,15,18,8,6,11),(19,'2024-08-06 15:02:00.000000','Team 1',5,11,18,8,11,6),(20,'2024-08-06 15:03:00.000000','Team 2',5,11,18,8,4,11),(21,'2024-08-06 15:03:00.000000','Team 1',5,11,18,15,11,5),(22,'2024-08-06 15:04:00.000000','Team 1',5,11,15,21,11,6),(23,'2024-08-06 15:04:00.000000','Team 2',5,11,18,8,9,11),(24,'2024-08-06 01:20:00.000000','Team 2',23,15,18,8,8,11),(25,'2024-08-06 01:20:00.000000','Team 1',5,23,18,8,11,9),(26,'2024-08-07 06:24:00.000000','Team 1',4,11,14,7,11,1),(27,'2024-08-07 06:25:00.000000','Team 1',4,11,1,2,11,3),(28,'2024-08-07 06:26:00.000000','Team 1',4,11,18,9,11,6),(29,'2024-08-07 06:27:00.000000','Team 1',11,4,12,24,11,7),(30,'2024-08-07 06:34:00.000000','Team 1',4,11,5,8,11,3),(31,'2024-08-07 06:36:00.000000','Team 1',11,4,12,13,11,7),(32,'2024-08-07 06:37:00.000000','Team 1',4,11,7,14,11,4),(33,'2024-08-07 06:43:00.000000','Team 1',4,11,1,2,11,8),(34,'2024-08-07 06:44:00.000000','Team 1',4,11,18,9,11,8),(35,'2024-08-07 06:48:00.000000','Team 1',11,4,5,8,11,7),(36,'2024-08-07 06:51:00.000000','Team 2',12,24,4,11,6,11),(37,'2024-08-07 06:55:00.000000','Team 1',4,11,12,13,11,6),(38,'2024-08-08 19:10:00.000000','Team 1',20,27,19,25,11,9),(39,'2024-08-08 19:11:00.000000','Team 2',20,27,4,1,7,11),(40,'2024-08-08 19:11:00.000000','Team 1',4,1,12,9,11,9),(41,'2024-08-08 19:12:00.000000','Team 1',11,18,4,1,11,3),(42,'2024-08-08 19:13:00.000000','Team 1',11,18,26,19,11,6),(43,'2024-08-08 19:14:00.000000','Team 1',11,18,13,10,11,3),(44,'2024-08-08 19:14:00.000000','Team 1',18,11,27,20,11,5),(45,'2024-08-08 19:15:00.000000','Team 1',18,11,12,9,11,9),(46,'2024-08-08 19:16:00.000000','Team 2',18,11,1,4,9,11),(47,'2024-08-08 19:16:00.000000','Team 2',15,5,1,4,6,11),(48,'2024-08-08 19:17:00.000000','Team 1',1,4,12,9,11,8),(49,'2024-08-08 14:17:00.000000','Team 2',12,21,15,18,9,11),(50,'2024-08-08 14:20:00.000000','Team 2',15,18,12,5,8,11),(51,'2024-08-08 13:05:00.000000','Team 1',12,5,15,18,11,9),(52,'2024-08-08 13:15:00.000000','Team 1',12,5,15,21,11,6),(53,'2024-08-08 13:20:00.000000','Team 1',12,5,18,21,11,5),(54,'2024-08-08 13:25:00.000000','Team 1',12,5,15,18,12,10),(55,'2024-08-08 13:30:00.000000','Team 1',5,18,15,23,12,10),(56,'2024-08-08 13:30:00.000000','Team 1',15,23,5,18,11,8),(57,'2024-08-08 13:35:00.000000','Team 1',15,23,5,18,11,8),(58,'2024-08-08 13:40:00.000000','Team 1',15,23,5,18,11,8),(59,'2024-08-08 13:45:00.000000','Team 1',15,23,5,18,11,8),(60,'2024-08-08 13:50:00.000000','Team 1',15,23,5,18,11,8),(61,'2024-08-09 11:15:00.000000','Team 2',21,15,9,5,7,11),(62,'2024-08-09 13:20:00.000000','Team 1',18,8,9,5,11,3),(63,'2024-08-09 13:55:00.000000','Team 1',11,28,18,8,11,8),(64,'2024-08-09 13:30:00.000000','Team 1',11,28,15,21,11,6),(65,'2024-08-09 13:35:00.000000','Team 2',11,28,9,5,6,11),(66,'2024-08-09 13:58:00.000000','Team 1',18,8,9,5,11,6),(67,'2024-08-09 13:45:00.000000','Team 1',18,8,21,15,11,9),(68,'2024-08-09 13:50:00.000000','Team 1',18,8,11,5,11,6),(69,'2024-08-09 13:55:00.000000','Team 1',18,8,21,15,11,9),(70,'2024-08-10 14:00:00.000000','Team 1',18,8,11,15,15,13),(71,'2024-08-09 14:05:00.000000','Team 1',18,8,21,15,11,2),(72,'2024-08-10 14:10:00.000000','Team 2',18,8,11,15,7,11),(73,'2024-08-09 14:15:00.000000','Team 2',18,6,11,15,4,11),(74,'2024-08-09 14:20:00.000000','Team 2',21,8,11,15,5,11),(75,'2024-08-09 14:25:00.000000','Team 1',18,8,11,15,15,13),(76,'2024-08-11 03:42:00.000000','Team 1',1,11,14,7,12,10),(77,'2024-08-11 03:43:00.000000','Team 1',12,9,1,11,11,5),(78,'2024-08-11 03:43:00.000000','Team 2',12,9,18,11,9,11),(79,'2024-08-11 03:44:00.000000','Team 2',7,14,18,11,7,11),(80,'2024-08-11 03:44:00.000000','Team 2',18,11,12,9,9,11),(81,'2024-08-11 03:45:00.000000','Team 1',12,9,1,2,11,0),(82,'2024-08-11 03:45:00.000000','Team 1',12,9,14,7,11,2),(83,'2024-08-11 03:46:00.000000','Team 1',12,9,1,5,11,4),(84,'2024-08-11 03:46:00.000000','Team 1',12,9,11,18,11,9),(85,'2024-08-11 04:26:00.000000','Team 1',12,28,8,23,11,9),(86,'2024-08-11 04:26:00.000000','Team 1',12,28,15,1,11,9),(87,'2024-08-11 04:27:00.000000','Team 1',12,28,5,1,11,7),(88,'2024-08-11 04:27:00.000000','Team 2',12,28,8,23,6,11),(89,'2024-08-11 04:28:00.000000','Team 2',15,5,8,23,6,11),(90,'2024-08-11 04:28:00.000000','Team 1',1,15,8,23,11,5),(91,'2024-08-11 04:28:00.000000','Team 2',1,15,12,28,5,11),(92,'2024-08-11 04:29:00.000000','Team 2',5,1,12,28,4,11),(93,'2024-08-11 04:29:00.000000','Team 2',5,1,12,28,4,11),(94,'2024-08-11 04:30:00.000000','Team 2',8,23,12,28,9,11),(95,'2024-08-11 04:30:00.000000','Team 1',1,15,12,28,11,6),(96,'2024-08-11 04:31:00.000000','Team 2',1,15,5,11,10,12),(97,'2024-08-11 04:31:00.000000','Team 2',8,23,5,11,12,14),(98,'2024-08-11 04:32:00.000000','Team 1',12,28,5,11,11,6),(100,'2024-08-11 04:34:00.000000','Team 1',12,28,1,15,11,6),(101,'2024-08-11 04:34:00.000000','Team 1',12,28,5,8,11,3),(102,'2024-08-11 04:35:00.000000','Team 1',12,28,1,15,11,7),(103,'2024-08-11 04:35:00.000000','Team 1',12,28,8,23,11,6),(104,'2024-08-12 06:00:00.000000','Team 1',19,26,25,27,11,8),(105,'2024-08-12 14:42:00.000000','Team 1',19,26,27,20,11,5),(106,'2024-08-12 14:43:00.000000','Team 2',19,26,25,20,7,11),(107,'2024-08-12 14:44:00.000000','Team 2',27,26,25,20,6,11),(108,'2024-08-12 14:44:00.000000','Team 1',29,20,19,25,11,9),(109,'2024-08-12 17:31:00.000000','Team 2',14,7,1,18,5,11),(110,'2024-08-12 17:31:00.000000','Team 2',1,18,12,9,9,11),(111,'2024-08-12 17:32:00.000000','Team 1',9,12,5,18,11,4),(112,'2024-08-12 17:32:00.000000','Team 1',9,12,5,15,11,8),(113,'2024-08-12 17:33:00.000000','Team 1',9,12,7,14,11,8),(114,'2024-08-12 17:33:00.000000','Team 1',9,12,1,18,11,9),(115,'2024-08-12 17:34:00.000000','Team 1',9,12,5,15,11,4),(116,'2024-08-12 17:35:00.000000','Team 1',9,12,7,14,11,7),(117,'2024-08-12 17:35:00.000000','Team 1',9,12,1,18,11,8),(118,'2024-08-12 17:35:00.000000','Team 1',9,12,5,15,12,10),(119,'2024-08-12 12:00:00.000000','Team 2',15,8,18,28,5,11),(120,'2024-08-12 12:10:00.000000','Team 2',15,8,18,28,7,11),(121,'2024-08-12 12:20:00.000000','Team 1',15,8,18,28,11,6),(122,'2024-08-12 12:25:00.000000','Team 2',15,28,18,5,9,11),(123,'2024-08-12 12:25:00.000000','Team 2',15,28,18,5,9,11),(124,'2024-08-12 12:30:00.000000','Team 2',8,28,18,5,9,11),(125,'2024-08-13 06:05:00.000000','Team 2',1,2,18,7,9,11),(126,'2024-08-13 07:52:00.000000','Team 1',4,11,18,7,11,3),(127,'2024-08-13 07:53:00.000000','Team 1',4,11,12,9,11,6),(128,'2024-08-13 07:53:00.000000','Team 1',4,11,1,2,11,3),(129,'2024-08-13 07:54:00.000000','Team 1',4,11,18,7,11,5),(130,'2024-08-13 07:54:00.000000','Team 1',4,11,12,9,11,8),(131,'2024-08-13 07:56:00.000000','Team 1',4,11,5,1,11,3),(132,'2024-08-13 07:56:00.000000','Team 1',4,11,5,23,11,5),(133,'2024-08-13 07:57:00.000000','Team 1',4,11,7,2,11,2),(134,'2024-08-13 07:57:00.000000','Team 1',4,11,12,9,11,6),(135,'2024-08-14 09:51:00.000000','Team 2',14,30,1,7,3,11),(136,'2024-08-14 09:52:00.000000','Team 2',1,7,4,11,8,11),(137,'2024-08-14 09:52:00.000000','Team 2',4,11,9,18,10,12),(138,'2024-08-14 09:53:00.000000','Team 1',9,18,14,7,11,4),(139,'2024-08-14 09:53:00.000000','Team 1',7,1,9,18,12,10),(140,'2024-08-14 09:53:00.000000','Team 2',7,1,4,11,5,11),(141,'2024-08-14 09:54:00.000000','Team 1',4,11,5,15,11,9),(142,'2024-08-14 09:54:00.000000','Team 1',4,11,14,7,11,5),(143,'2024-08-14 09:55:00.000000','Team 1',4,5,9,18,11,9),(144,'2024-08-15 07:06:00.000000','Team 1',12,13,1,15,11,5),(145,'2024-08-15 07:06:00.000000','Team 2',12,13,9,18,8,11),(146,'2024-08-15 07:07:00.000000','Team 1',5,15,9,18,11,9),(147,'2024-08-15 07:13:00.000000','Team 2',5,15,1,2,9,11),(148,'2024-08-15 07:15:00.000000','Team 1',12,13,1,2,11,9),(149,'2024-08-15 07:15:00.000000','Team 1',12,13,9,18,11,4),(150,'2024-08-15 07:16:00.000000','Team 1',12,13,5,15,11,7),(151,'2024-08-15 07:17:00.000000','Team 1',12,13,1,2,11,3),(152,'2024-08-15 11:00:00.000000','Team 2',18,15,9,8,7,11),(153,'2024-08-15 11:05:00.000000','Team 1',18,15,9,8,11,8),(154,'2024-08-15 11:10:00.000000','Team 2',18,15,9,8,9,11),(155,'2024-08-15 11:15:00.000000','Team 2',18,15,9,8,7,11),(156,'2024-08-15 11:20:00.000000','Team 1',18,15,9,8,11,6),(157,'2024-08-15 11:25:00.000000','Team 1',18,15,9,8,11,7),(158,'2024-08-15 11:30:00.000000','Team 2',23,9,18,15,7,11),(159,'2024-08-15 11:35:00.000000','Team 2',23,15,9,8,9,11),(160,'2024-08-15 11:40:00.000000','Team 2',23,18,9,8,6,11),(161,'2024-08-15 11:45:00.000000','Team 2',18,15,9,8,11,13),(162,'2024-08-15 11:50:00.000000','Team 1',18,15,9,8,11,8),(163,'2024-08-15 11:55:00.000000','Team 1',18,15,9,8,11,6),(164,'2024-08-15 12:00:00.000000','Team 1',18,15,9,8,11,9),(165,'2024-08-15 12:05:00.000000',NULL,18,15,9,8,10,9),(166,'2024-08-15 12:10:00.000000','Team 2',18,15,9,8,9,11),(167,'2024-08-15 12:15:00.000000','Team 1',18,15,9,8,11,3),(168,'2024-08-15 12:20:00.000000','Team 2',18,15,9,8,7,11),(169,'2024-08-16 07:09:00.000000','Team 1',7,30,14,1,12,10),(170,'2024-08-16 07:10:00.000000','Team 2',30,7,1,2,8,11),(171,'2024-08-16 07:10:00.000000','Team 2',1,2,12,9,7,11),(172,'2024-08-16 07:11:00.000000','Team 1',12,9,5,18,11,9),(173,'2024-08-16 07:11:00.000000','Team 1',12,9,15,18,11,5),(174,'2024-08-16 07:12:00.000000','Team 1',12,9,14,1,11,5),(175,'2024-08-16 07:12:00.000000','Team 1',12,9,7,30,11,0),(176,'2024-08-16 07:13:00.000000','Team 1',12,9,1,2,11,9),(177,'2024-08-16 07:13:00.000000','Team 1',12,9,18,5,11,7),(178,'2024-08-20 15:06:00.000000','Team 2',14,7,1,2,9,11),(179,'2024-08-20 15:10:00.000000','Team 2',1,2,12,9,8,11),(180,'2024-08-20 15:12:00.000000','Team 1',12,9,18,11,11,7),(181,'2024-08-20 15:12:00.000000','Team 1',12,9,18,11,11,7),(182,'2024-08-20 15:13:00.000000','Team 1',12,9,14,7,11,9),(183,'2024-08-20 15:14:00.000000','Team 1',12,9,1,2,11,0),(184,'2024-08-20 15:14:00.000000','Team 1',12,9,18,11,11,6),(185,'2024-08-20 15:15:00.000000','Team 1',12,9,14,7,11,1),(186,'2024-08-20 15:17:00.000000','Team 1',12,9,1,2,11,8),(187,'2024-08-20 15:17:00.000000','Team 1',12,9,18,11,11,4),(188,'2024-08-20 15:18:00.000000','Team 1',12,9,14,7,11,6),(189,'2024-08-20 15:18:00.000000','Team 1',12,9,1,2,11,8),(190,'2024-08-20 15:19:00.000000','Team 1',12,9,18,11,11,2),(191,'2024-08-20 15:22:00.000000','Team 1',1,2,7,18,11,6),(192,'2024-08-20 15:22:00.000000','Team 2',1,2,11,4,11,13),(193,'2024-08-20 15:23:00.000000','Team 2',12,9,11,4,6,11),(194,'2024-08-20 15:23:00.000000','Team 2',5,18,11,4,9,11),(195,'2024-08-20 15:24:00.000000','Team 2',7,18,11,4,2,11),(196,'2024-08-20 15:25:00.000000','Team 2',12,9,11,4,7,11),(197,'2024-08-20 15:25:00.000000','Team 2',5,18,11,4,13,15),(198,'2024-08-14 07:24:00.000000','Team 1',9,18,5,15,11,6),(199,'2024-08-21 08:44:00.000000','Team 2',14,30,1,7,7,11),(200,'2024-08-21 08:45:00.000000','Team 2',1,7,9,2,4,11),(201,'2024-08-21 08:45:00.000000','Team 2',2,9,12,1,0,11),(202,'2024-08-21 08:46:00.000000','Team 1',12,1,4,18,11,7),(203,'2024-08-21 08:47:00.000000','Team 1',12,1,8,5,11,7),(204,'2024-08-21 08:47:00.000000','Team 1',12,1,14,30,11,0),(205,'2024-08-21 08:48:00.000000','Team 1',12,1,2,9,11,4),(206,'2024-08-21 08:50:00.000000','Team 1',12,1,18,4,11,7),(207,'2024-08-21 08:51:00.000000','Team 1',12,1,8,5,11,6),(208,'2024-08-21 08:51:00.000000','Team 1',12,1,2,9,12,10),(209,'2024-08-22 08:18:00.000000','Team 1',1,22,12,25,12,10),(210,'2024-08-22 12:00:00.000000','Team 2',5,8,11,23,5,11),(211,'2024-08-22 12:05:00.000000','Team 2',8,18,11,23,8,11),(212,'2024-08-22 12:10:00.000000','Team 2',5,18,11,23,9,11),(213,'2024-08-22 12:15:00.000000','Team 1',18,8,11,23,11,8),(214,'2024-08-22 12:20:00.000000','Team 1',5,11,8,18,11,8),(215,'2024-08-22 12:25:00.000000','Team 1',5,11,8,28,11,8),(216,'2024-08-22 12:25:00.000000','Team 1',5,11,8,28,11,6),(217,'2024-08-22 12:30:00.000000','Team 1',5,11,8,18,11,6),(218,'2024-08-22 12:40:00.000000','Team 1',5,11,18,8,11,4),(219,'2024-08-22 12:45:00.000000','Team 2',5,11,18,8,5,11),(220,'2024-08-27 06:20:00.000000','Team 1',5,9,1,8,11,8),(221,'2024-08-27 06:25:00.000000','Team 1',4,11,5,9,11,8),(222,'2024-08-27 06:28:00.000000','Team 1',4,11,18,15,11,8),(223,'2024-08-27 06:30:00.000000','Team 1',4,11,5,9,15,13),(224,'2024-08-27 06:35:00.000000','Team 1',4,11,18,8,11,8),(225,'2024-08-27 06:35:00.000000','Team 1',4,11,1,8,11,8),(226,'2024-08-27 06:39:00.000000','Team 1',4,11,1,8,11,8),(227,'2024-08-27 06:40:00.000000','Team 1',4,11,5,9,11,8),(228,'2024-08-27 06:43:00.000000','Team 1',4,11,18,8,11,8),(229,'2024-08-27 06:48:00.000000','Team 1',4,11,5,9,11,8),(230,'2024-08-27 06:50:00.000000','Team 1',4,11,1,8,11,8),(231,'2024-08-28 07:28:00.000000','Team 1',1,18,20,19,11,4),(232,'2024-08-28 07:28:00.000000','Team 1',1,18,5,4,11,8),(233,'2024-08-28 07:29:00.000000','Team 1',1,18,12,24,11,5),(234,'2024-08-28 07:30:00.000000','Team 2',1,18,9,15,6,11),(235,'2024-08-28 07:30:00.000000','Team 1',4,11,15,9,11,3),(236,'2024-08-28 07:31:00.000000','Team 1',4,11,20,27,11,1),(237,'2024-08-28 07:32:00.000000','Team 1',4,11,5,15,11,9),(238,'2024-08-28 07:32:00.000000','Team 1',4,11,12,24,11,7),(239,'2024-08-28 07:33:00.000000','Team 2',1,18,4,11,6,11),(240,'2024-08-28 07:33:00.000000','Team 1',4,11,9,15,11,9),(254,'2024-08-30 16:55:00.000000','Team 1',1,18,8,9,11,6),(255,'2024-08-30 16:56:00.000000','Team 1',1,18,12,9,12,10),(256,'2024-08-30 16:56:00.000000','Team 1',1,18,9,15,11,6),(257,'2024-08-30 16:56:00.000000','Team 2',1,18,12,8,4,11),(258,'2024-08-30 16:57:00.000000','Team 2',11,15,12,8,2,11),(259,'2024-08-30 16:57:00.000000','Team 2',9,15,12,8,3,11),(260,'2024-08-30 16:57:00.000000','Team 2',1,18,12,8,4,11),(261,'2024-09-10 06:21:00.000000','Team 1',18,31,1,17,11,7),(262,'2024-09-10 06:22:00.000000','Team 2',18,31,12,9,4,11),(263,'2024-09-10 06:24:00.000000','Team 2',4,5,12,9,4,11),(264,'2024-09-10 06:28:00.000000','Team 1',11,13,12,9,11,7),(265,'2024-09-10 06:28:00.000000','Team 1',11,13,12,9,11,7),(266,'2024-09-10 06:37:00.000000','Team 1',11,13,2,7,11,5),(267,'2024-09-10 06:45:00.000000','Team 1',11,13,15,29,11,5),(268,'2024-09-10 06:45:00.000000','Team 1',11,13,1,17,11,7),(269,'2024-09-10 06:49:00.000000','Team 1',11,13,18,31,11,9),(270,'2024-09-10 06:53:00.000000','Team 2',11,13,12,9,8,11),(271,'2024-09-10 06:56:00.000000','Team 2',4,5,12,9,9,11),(272,'2024-09-11 06:19:00.000000','Team 1',7,2,1,19,11,9),(273,'2024-09-11 06:25:00.000000','Team 2',7,2,12,24,10,12),(274,'2024-09-11 06:35:00.000000','Team 1',15,18,12,24,13,11),(275,'2024-09-11 06:35:00.000000','Team 1',15,18,1,22,11,6),(276,'2024-09-11 06:38:00.000000','Team 1',15,18,11,13,11,5),(277,'2024-09-11 06:41:00.000000','Team 1',15,18,5,9,11,0),(278,'2024-09-11 06:41:00.000000','Team 1',15,18,1,19,11,0),(279,'2024-09-11 06:42:00.000000','Team 1',15,18,7,2,11,5),(280,'2024-09-11 06:52:00.000000','Team 1',15,18,12,24,11,4),(281,'2024-09-11 06:52:00.000000','Team 1',15,18,22,9,11,0),(282,'2024-09-11 06:56:00.000000','Team 1',15,18,11,13,11,8),(283,'2024-09-11 06:57:00.000000','Team 1',15,18,1,9,11,4),(284,'2024-09-12 06:22:00.000000','Team 2',1,9,13,11,6,11),(285,'2024-09-12 06:22:00.000000','Team 1',18,31,13,11,11,9),(286,'2024-09-12 06:27:00.000000','Team 1',18,31,15,5,13,11),(287,'2024-09-12 06:37:00.000000','Team 1',18,31,9,1,11,9),(288,'2024-09-12 06:37:00.000000','Team 1',18,31,13,11,11,5),(289,'2024-09-12 06:41:00.000000','Team 2',18,31,15,5,6,11),(290,'2024-09-12 06:47:00.000000','Team 2',1,9,15,5,4,11),(291,'2024-09-12 06:47:00.000000','Team 1',13,11,15,5,11,6),(292,'2024-09-12 06:51:00.000000','Team 2',13,11,18,31,9,11),(293,'2024-09-12 06:59:00.000000','Team 2',9,1,18,31,9,11),(294,'2024-09-13 06:27:00.000000','Team 2',2,7,1,15,4,11),(295,'2024-09-13 06:28:00.000000','Team 1',12,9,15,1,11,9),(296,'2024-09-13 06:29:00.000000','Team 1',12,9,1,11,11,9),(297,'2024-09-13 06:29:00.000000','Team 1',12,9,15,5,11,7),(298,'2024-09-13 06:32:00.000000','Team 1',12,9,18,31,11,6),(299,'2024-09-13 06:43:00.000000','Team 1',12,9,2,7,11,4),(300,'2024-09-13 06:44:00.000000','Team 1',12,9,1,11,11,8),(301,'2024-09-13 06:44:00.000000','Team 1',12,9,15,5,11,8),(302,'2024-09-13 06:46:00.000000','Team 1',12,9,18,31,11,6),(303,'2024-09-13 06:58:00.000000','Team 1',12,9,2,7,11,6),(304,'2024-09-13 06:59:00.000000','Team 2',12,9,1,11,9,11),(305,'2024-09-13 07:00:00.000000','Team 2',15,5,1,11,4,11),(306,'2024-09-17 08:09:00.000000','Team 2',14,19,1,7,8,11),(307,'2024-09-17 08:11:00.000000','Team 1',1,7,29,17,11,5),(308,'2024-09-17 08:13:00.000000','Team 1',1,7,12,24,11,9),(309,'2024-09-17 08:13:00.000000','Team 2',1,7,18,31,10,12),(310,'2024-09-17 08:14:00.000000','Team 2',18,31,9,13,9,11),(311,'2024-09-17 08:14:00.000000','Team 2',9,13,5,15,8,11),(312,'2024-09-17 08:15:00.000000','Team 2',5,15,1,2,7,11),(313,'2024-09-17 08:17:00.000000','Team 1',1,2,29,17,11,5),(314,'2024-09-17 08:18:00.000000','Team 1',1,2,19,20,11,7),(315,'2024-09-17 08:18:00.000000','Team 1',1,2,12,24,11,6),(316,'2024-09-17 08:20:00.000000','Team 2',1,2,18,31,6,11),(317,'2024-09-18 07:00:00.000000','Team 1',1,2,29,22,11,3),(318,'2024-09-18 07:01:00.000000','Team 1',1,2,18,15,13,11),(319,'2024-09-18 07:01:00.000000','Team 2',14,7,1,2,5,11),(320,'2024-09-18 07:02:00.000000','Team 1',1,2,12,24,11,6),(321,'2024-09-18 07:02:00.000000','Team 2',1,2,13,18,10,12),(322,'2024-09-18 07:05:00.000000','Team 1',13,18,19,20,11,5),(323,'2024-09-18 07:03:00.000000','Team 2',13,18,12,24,7,11),(324,'2024-09-18 07:04:00.000000','Team 2',12,24,1,22,6,11),(325,'2024-09-18 07:05:00.000000','Team 1',1,22,25,27,11,6),(326,'2024-09-19 06:20:00.000000','Team 2',1,22,7,29,10,12),(327,'2024-09-19 06:21:00.000000','Team 1',12,9,7,29,11,5),(328,'2024-09-19 06:23:00.000000','Team 1',12,9,31,18,11,6),(329,'2024-09-19 06:38:00.000000','Team 1',12,9,5,15,11,6),(330,'2024-09-19 06:38:00.000000','Team 1',12,9,1,22,11,9),(331,'2024-09-20 06:14:00.000000','Team 1',1,2,29,19,11,7),(332,'2024-09-20 06:19:00.000000','Team 2',1,2,18,31,3,11),(333,'2024-09-20 06:24:00.000000','Team 1',12,9,18,31,11,9),(334,'2024-09-20 06:35:00.000000','Team 1',12,9,19,20,11,4),(335,'2024-09-20 06:38:00.000000','Team 2',12,9,1,2,9,11),(336,'2024-09-20 06:41:00.000000','Team 1',1,2,29,17,11,5),(337,'2024-09-20 06:44:00.000000','Team 1',1,2,18,31,12,10),(338,'2024-09-20 06:50:00.000000','Team 1',1,2,5,15,11,4),(339,'2024-09-20 06:52:00.000000','Team 2',12,9,1,2,9,11),(340,'2024-09-20 06:31:00.000000','Team 1',12,9,5,15,11,7),(341,'2024-09-23 06:05:00.000000','Team 1',1,22,19,29,11,7),(342,'2024-09-23 06:10:00.000000','Team 2',1,22,20,27,7,11),(343,'2024-09-23 06:17:00.000000','Team 1',18,31,27,20,11,3),(344,'2024-09-23 06:22:00.000000','Team 1',18,31,12,24,11,3),(345,'2024-09-23 06:27:00.000000','Team 1',18,31,5,9,11,5),(346,'2024-09-23 06:30:00.000000','Team 1',18,31,29,19,11,3),(347,'2024-09-23 06:33:00.000000','Team 1',18,31,22,1,11,7),(348,'2024-09-23 06:36:00.000000','Team 1',18,31,20,27,11,2),(349,'2024-09-23 06:38:00.000000','Team 1',18,31,12,24,11,6),(350,'2024-09-23 06:41:00.000000','Team 2',5,9,18,31,9,11),(351,'2024-09-23 06:45:00.000000','Team 2',19,29,18,31,5,11),(352,'2024-09-23 06:49:00.000000','Team 1',18,31,1,22,12,10),(353,'2024-09-23 06:53:00.000000','Team 2',18,31,12,27,2,11),(354,'2024-09-25 09:54:00.000000','Team 2',1,19,20,27,9,11),(355,'2024-09-25 09:54:00.000000','Team 1',14,7,20,27,11,5),(356,'2024-09-25 09:55:00.000000','Team 2',14,7,12,24,9,11),(357,'2024-09-25 09:55:00.000000','Team 1',18,15,29,9,11,0),(358,'2024-09-25 09:56:00.000000','Team 1',18,15,1,2,12,10),(359,'2024-09-25 09:56:00.000000','Team 1',18,15,20,19,11,2),(360,'2024-09-25 09:56:00.000000','Team 1',18,15,7,14,11,8),(361,'2024-09-25 09:57:00.000000','Team 1',18,15,12,24,11,7),(362,'2024-09-25 09:57:00.000000','Team 2',18,15,29,9,7,11),(363,'2024-09-27 07:52:00.000000','Team 1',1,7,19,20,11,9),(364,'2024-09-27 07:53:00.000000','Team 2',1,7,2,9,8,11),(365,'2024-09-27 07:53:00.000000','Team 2',12,22,2,9,6,11),(366,'2024-09-27 07:54:00.000000','Team 2',19,20,2,9,5,11),(367,'2024-09-27 07:54:00.000000','Team 1',31,18,2,9,11,4),(368,'2024-09-27 07:54:00.000000','Team 1',31,18,5,15,11,6),(369,'2024-09-27 07:55:00.000000','Team 1',31,18,1,7,12,10),(370,'2024-09-27 07:56:00.000000','Team 1',31,18,2,9,11,4),(371,'2024-09-27 07:56:00.000000','Team 2',31,18,22,12,6,11),(372,'2024-09-27 07:56:00.000000','Team 2',20,19,22,12,3,11),(373,'2024-10-11 14:29:00.000000','Team 1',7,19,9,20,11,9),(374,'2024-10-11 14:30:00.000000','Team 2',7,19,27,25,9,11),(375,'2024-10-11 14:30:00.000000','Team 2',27,25,2,22,7,11),(376,'2024-10-11 14:31:00.000000','Team 1',1,9,2,22,11,6),(377,'2024-10-11 14:31:00.000000','Team 1',1,9,7,19,11,6),(378,'2024-10-11 14:32:00.000000','Team 1',1,9,7,19,11,6),(379,'2024-10-11 14:32:00.000000','Team 1',1,9,27,25,11,6),(380,'2024-10-11 14:33:00.000000','Team 1',1,9,27,25,11,6),(381,'2024-10-11 14:33:00.000000','Team 1',1,9,2,22,11,6),(382,'2024-10-11 14:33:00.000000','Team 1',1,9,2,22,11,6),(383,'2024-10-15 14:34:00.000000','Team 1',1,2,22,19,11,8),(384,'2024-10-15 14:35:00.000000','Team 2',1,2,9,15,9,11),(385,'2024-10-15 14:35:00.000000','Team 1',9,15,20,27,11,6),(386,'2024-10-15 14:36:00.000000','Team 1',9,15,5,17,11,6),(387,'2024-10-15 14:36:00.000000','Team 1',9,15,12,24,11,6),(388,'2024-10-15 14:37:00.000000','Team 1',1,2,9,15,11,7),(389,'2024-10-15 14:37:00.000000','Team 1',1,2,27,20,11,3),(390,'2024-10-15 14:38:00.000000','Team 1',1,2,5,17,11,5),(391,'2024-10-15 14:38:00.000000','Team 1',1,2,25,22,11,4),(392,'2024-10-15 14:39:00.000000','Team 2',12,24,1,2,4,11),(393,'2024-10-15 14:39:00.000000','Team 1',1,2,9,15,11,6),(394,'2024-10-15 14:40:00.000000','Team 1',1,2,5,17,11,3),(395,'2024-10-15 14:40:00.000000','Team 2',1,2,12,24,9,11),(396,'2024-10-16 06:13:00.000000','Team 1',1,2,19,25,11,3),(397,'2024-10-16 06:19:00.000000','Team 1',1,2,11,7,11,9),(398,'2024-10-16 06:19:00.000000','Team 2',1,2,9,13,5,11),(399,'2024-10-16 06:33:00.000000','Team 1',12,24,13,9,12,10),(400,'2024-10-16 06:37:00.000000','Team 1',12,24,11,17,11,8),(401,'2024-10-16 06:40:00.000000','Team 1',12,24,19,7,11,6),(402,'2024-10-16 06:45:00.000000','Team 1',12,24,1,2,14,12),(403,'2024-10-16 06:48:00.000000','Team 2',12,24,9,13,7,11),(404,'2024-10-16 06:52:00.000000','Team 1',19,7,9,13,11,9),(405,'2024-10-16 06:58:00.000000','Team 2',19,7,11,17,2,11),(406,'2024-10-16 07:00:00.000000','Team 1',1,2,11,17,11,8),(407,'2024-10-17 06:20:00.000000','Team 1',1,11,9,15,11,8),(408,'2024-10-17 06:22:00.000000','Team 1',1,11,2,18,11,9),(409,'2024-10-17 06:26:00.000000','Team 1',1,11,7,19,11,6),(410,'2024-10-17 06:26:00.000000','Team 1',1,11,12,22,11,5),(411,'2024-10-17 06:30:00.000000','Team 1',1,11,15,9,11,9),(412,'2024-10-17 06:38:00.000000','Team 1',11,26,18,2,11,9),(413,'2024-10-17 06:39:00.000000','Team 1',11,1,12,22,11,7),(414,'2024-10-17 06:41:00.000000','Team 1',11,1,19,7,11,3),(415,'2024-10-17 06:43:00.000000','Team 1',11,1,15,9,11,3),(416,'2024-10-17 06:49:00.000000','Team 1',11,1,18,2,11,5),(417,'2024-10-17 06:49:00.000000','Team 2',11,1,22,12,9,11),(418,'2024-10-17 06:53:00.000000','Team 1',12,22,19,2,11,9),(419,'2024-10-17 06:57:00.000000','Team 2',12,22,15,9,6,11),(420,'2024-10-18 06:40:00.000000','Team 1',1,13,7,20,11,4),(421,'2024-10-18 06:40:00.000000','Team 1',1,13,19,2,13,11),(422,'2024-10-23 06:27:00.000000','Team 1',2,22,17,7,12,10),(423,'2024-10-23 06:28:00.000000','Team 1',11,1,2,22,12,10),(424,'2024-10-23 06:33:00.000000','Team 1',11,1,9,15,11,7),(425,'2024-10-23 06:37:00.000000','Team 1',11,1,2,5,11,4),(426,'2024-10-23 06:45:00.000000','Team 1',11,1,7,17,11,6),(427,'2024-10-23 06:46:00.000000','Team 1',11,1,24,12,14,12),(428,'2024-10-23 06:55:00.000000','Team 2',11,1,15,9,9,11),(429,'2024-10-23 06:55:00.000000','Team 2',22,2,15,9,8,11),(430,'2024-10-23 06:55:00.000000','Team 1',12,24,15,9,12,10),(431,'2024-10-24 06:20:00.000000','Team 2',7,29,11,1,6,11),(432,'2024-10-24 06:30:00.000000','Team 2',9,12,11,1,5,11),(433,'2024-10-24 06:34:00.000000','Team 2',20,19,11,1,5,11),(434,'2024-10-24 06:38:00.000000','Team 2',5,7,11,1,6,11),(435,'2024-10-24 06:41:00.000000','Team 2',25,29,11,1,5,11),(436,'2024-10-24 06:45:00.000000','Team 2',9,12,11,1,9,11),(437,'2024-10-24 06:50:00.000000','Team 2',19,20,11,1,12,14),(438,'2024-10-24 06:50:00.000000','Team 2',5,7,11,1,5,11),(439,'2024-10-24 06:59:00.000000','Team 2',25,27,11,1,5,11),(440,'2024-10-24 07:00:00.000000','Team 2',12,9,11,1,6,11),(441,'2024-10-25 06:20:00.000000','Team 2',7,14,1,2,9,11),(442,'2024-10-25 06:27:00.000000','Team 2',12,22,1,2,8,11),(443,'2024-10-25 06:34:00.000000','Team 2',11,5,1,2,8,11),(444,'2024-10-25 06:39:00.000000','Team 2',19,20,1,2,9,11),(445,'2024-10-25 06:42:00.000000','Team 1',12,9,1,2,11,5),(446,'2024-10-25 06:51:00.000000','Team 1',12,9,7,22,11,5),(447,'2024-10-25 06:52:00.000000','Team 1',12,9,5,11,11,9),(448,'2024-10-25 06:54:00.000000','Team 1',12,9,19,20,12,10),(449,'2024-11-07 06:19:00.000000','Team 2',32,7,1,29,9,11),(450,'2024-11-07 06:28:00.000000','Team 1',12,19,1,29,11,7),(451,'2024-11-07 06:35:00.000000','Team 1',12,19,13,9,11,4),(452,'2024-11-07 06:35:00.000000','Team 2',24,29,1,2,4,11),(453,'2024-11-07 06:36:00.000000','Team 2',17,9,2,1,5,11),(454,'2024-11-07 06:36:00.000000','Team 1',1,2,22,12,11,7),(455,'2024-11-07 06:37:00.000000','Team 1',2,1,27,20,11,4),(456,'2024-11-07 06:37:00.000000','Team 2',29,24,2,1,9,11),(457,'2024-11-07 06:38:00.000000','Team 1',2,1,7,30,11,4),(458,'2024-11-07 06:38:00.000000','Team 2',12,19,5,11,4,11),(459,'2024-11-07 10:39:00.000000','Team 2',12,22,2,1,9,11),(460,'2024-11-07 06:40:00.000000','Team 1',1,2,5,9,11,7),(461,'2024-11-07 06:42:00.000000','Team 2',7,32,11,5,6,11),(462,'2024-11-07 06:45:00.000000','Team 1',1,29,5,11,11,9),(463,'2024-11-07 06:49:00.000000','Team 2',1,29,13,9,9,11),(464,'2024-11-07 06:53:00.000000','Team 1',12,19,5,11,11,9),(465,'2024-11-07 06:56:00.000000','Team 1',12,19,11,5,11,8),(466,'2024-11-07 06:59:00.000000','Team 1',12,19,7,32,11,6),(467,'2024-11-07 19:02:00.000000','Team 1',13,32,19,29,11,0),(468,'2024-11-07 19:03:00.000000','Team 2',13,32,12,24,5,11),(469,'2024-11-07 19:03:00.000000','Team 2',5,9,12,24,9,11),(470,'2024-11-07 19:04:00.000000','Team 2',1,2,12,24,9,11),(471,'2024-11-07 19:04:00.000000','Team 2',13,15,12,24,8,11),(472,'2024-11-07 19:05:00.000000','Team 2',19,7,12,24,6,11),(473,'2024-11-07 19:05:00.000000','Team 1',5,9,12,24,11,6),(474,'2024-11-07 19:05:00.000000','Team 1',5,9,22,29,11,4),(475,'2024-11-07 19:06:00.000000','Team 1',15,9,17,29,11,4),(476,'2024-11-07 19:08:00.000000','Team 1',15,9,1,2,11,9),(477,'2024-11-08 06:30:00.000000','Team 1',7,1,2,29,11,5),(478,'2024-11-08 06:30:00.000000','Team 1',7,1,2,17,11,8),(479,'2024-11-08 06:31:00.000000','Team 2',7,1,15,9,8,11),(480,'2024-11-08 06:32:00.000000','Team 2',2,29,15,9,2,11),(481,'2024-11-08 06:36:00.000000','Team 2',2,17,15,9,8,11),(482,'2024-11-08 06:39:00.000000','Team 2',7,1,9,15,6,11),(483,'2024-11-08 06:43:00.000000','Team 2',2,29,9,15,2,11),(484,'2024-11-08 06:47:00.000000','Team 2',2,17,9,15,8,11),(485,'2024-11-08 06:50:00.000000','Team 1',7,1,9,15,11,7),(486,'2024-11-08 06:55:00.000000','Team 2',7,1,2,29,9,11),(487,'2024-11-11 09:51:00.000000','Team 1',9,1,12,24,11,7),(488,'2024-11-11 09:51:00.000000','Team 1',9,1,24,32,11,3),(489,'2024-11-11 09:52:00.000000','Team 1',9,1,12,24,11,9),(490,'2024-11-11 09:52:00.000000','Team 1',9,1,5,32,11,6),(491,'2024-11-11 09:52:00.000000','Team 2',9,1,12,24,3,11),(492,'2024-11-11 09:53:00.000000','Team 2',5,32,12,24,7,11),(493,'2024-11-11 09:53:00.000000','Team 1',9,1,12,24,11,9),(494,'2024-11-11 09:54:00.000000','Team 1',9,1,5,32,11,7),(495,'2024-11-11 09:54:00.000000','Team 1',9,1,12,24,11,9),(496,'2024-11-11 09:54:00.000000','Team 2',9,24,1,22,7,11),(497,'2024-11-13 06:19:00.000000','Team 2',19,24,22,1,8,11),(498,'2024-11-13 06:20:00.000000','Team 1',2,7,1,22,12,10),(499,'2024-11-13 06:26:00.000000','Team 2',2,7,12,24,7,11),(500,'2024-11-13 06:34:00.000000','Team 2',29,9,1,22,9,11),(501,'2024-11-13 06:37:00.000000','Team 1',22,1,17,5,11,7),(502,'2024-11-13 06:46:00.000000','Team 1',1,22,2,7,11,8),(503,'2024-11-13 06:50:00.000000','Team 1',12,24,22,1,12,10),(504,'2024-11-13 06:54:00.000000','Team 1',12,24,29,9,11,5),(505,'2024-11-13 06:57:00.000000','Team 1',12,24,5,17,11,9),(506,'2024-11-12 07:02:00.000000','Team 1',29,9,2,7,11,8),(507,'2024-11-12 07:06:00.000000','Team 1',29,9,5,17,11,9),(508,'2024-11-12 07:06:00.000000','Team 1',29,9,1,25,11,5),(509,'2024-11-12 07:07:00.000000','Team 1',29,9,27,20,11,4),(510,'2024-11-12 07:08:00.000000','Team 1',29,9,2,7,11,8),(511,'2024-11-12 07:09:00.000000','Team 1',29,9,5,17,11,2),(512,'2024-11-12 07:09:00.000000','Team 2',29,9,1,25,8,11),(513,'2024-11-12 07:10:00.000000','Team 2',27,20,1,25,3,11),(514,'2024-11-12 07:10:00.000000','Team 1',2,7,1,25,11,9),(515,'2024-11-12 07:11:00.000000','Team 1',2,7,5,17,11,6),(516,'2024-11-14 06:32:00.000000','Team 1',22,1,29,7,11,9),(517,'2024-11-14 06:37:00.000000','Team 1',22,1,20,27,12,10),(518,'2024-11-14 06:41:00.000000','Team 2',34,32,20,27,1,11),(519,'2024-11-14 06:44:00.000000','Team 1',29,7,20,27,11,9),(520,'2024-11-14 06:49:00.000000','Team 1',29,7,19,35,11,4),(521,'2024-11-14 06:54:00.000000','Team 1',29,7,22,1,11,7),(522,'2024-11-14 06:58:00.000000','Team 1',29,7,20,27,12,10),(523,'2024-11-15 06:21:00.000000','Team 1',1,2,22,18,11,5),(524,'2024-11-15 06:25:00.000000','Team 1',1,2,11,7,11,8),(525,'2024-11-15 06:31:00.000000','Team 1',2,1,29,9,11,6),(526,'2024-11-15 06:38:00.000000','Team 2',1,2,15,12,5,11),(527,'2024-11-15 06:41:00.000000','Team 2',17,14,12,15,3,11),(528,'2024-11-15 06:44:00.000000','Team 2',18,22,12,15,6,11),(529,'2024-11-15 06:48:00.000000','Team 2',11,5,12,15,7,11),(530,'2024-11-15 06:52:00.000000','Team 1',11,7,12,15,11,6),(531,'2024-11-15 06:54:00.000000','Team 2',11,7,9,29,4,11),(532,'2024-11-15 06:57:00.000000','Team 2',9,29,1,2,4,11),(533,'2024-11-15 11:58:00.000000','Team 1',1,18,11,2,11,3),(534,'2024-11-15 12:01:00.000000','Team 1',18,1,12,22,11,3),(535,'2024-11-15 12:06:00.000000','Team 1',1,18,8,36,11,4),(536,'2024-11-15 12:10:00.000000','Team 1',1,18,11,16,11,7),(537,'2024-11-15 12:17:00.000000','Team 1',1,18,12,22,13,11),(538,'2024-11-15 12:22:00.000000','Team 2',18,1,8,36,7,11),(539,'2024-11-15 12:25:00.000000','Team 1',11,18,8,36,11,2),(540,'2024-11-15 12:28:00.000000','Team 2',11,18,12,22,6,11),(541,'2024-11-15 12:32:00.000000','Team 1',12,22,16,1,11,4),(542,'2024-11-15 12:35:00.000000','Team 1',8,36,12,22,11,8),(543,'2024-11-15 12:39:00.000000','Team 2',8,36,16,1,4,11),(544,'2024-11-15 12:51:00.000000','Team 1',12,22,8,36,11,9),(545,'2024-11-15 12:51:00.000000','Team 1',12,22,16,1,11,4),(546,'2024-11-15 12:51:00.000000','Team 1',12,22,16,1,11,9),(547,'2024-11-15 12:52:00.000000','Team 1',12,22,8,36,11,9),(548,'2024-11-15 12:57:00.000000','Team 2',12,22,16,1,8,11),(549,'2024-11-15 13:02:00.000000','Team 2',8,36,16,1,6,11),(550,'2024-11-18 06:14:00.000000','Team 1',33,1,29,22,11,7),(551,'2024-11-18 06:19:00.000000','Team 1',33,1,29,18,11,9),(552,'2024-11-18 06:25:00.000000','Team 2',33,1,12,24,10,12),(553,'2024-11-18 06:27:00.000000','Team 2',12,24,9,22,4,11),(554,'2024-11-18 06:32:00.000000','Team 1',22,9,19,5,11,7),(555,'2024-11-18 06:38:00.000000','Team 2',18,29,9,22,8,11),(556,'2024-11-18 06:41:00.000000','Team 1',9,22,1,33,12,10),(557,'2024-11-18 06:48:00.000000','Team 2',9,22,12,24,4,11),(558,'2024-11-18 06:52:00.000000','Team 2',19,5,12,24,9,11),(559,'2024-11-18 06:56:00.000000','Team 2',18,29,12,24,9,11),(560,'2024-11-19 06:18:00.000000','Team 1',1,18,2,9,11,6),(561,'2024-11-19 06:26:00.000000','Team 1',26,18,12,24,11,9),(562,'2024-11-19 06:34:00.000000','Team 1',1,18,29,22,11,5),(563,'2024-11-19 06:36:00.000000','Team 1',1,18,20,27,11,4),(564,'2024-11-19 06:39:00.000000','Team 1',1,18,7,17,11,6),(565,'2024-11-19 06:43:00.000000','Team 1',1,18,2,9,13,11),(566,'2024-11-19 07:01:00.000000','Team 1',1,18,17,5,11,7),(567,'2024-11-19 07:01:00.000000','Team 1',1,18,12,24,11,9),(568,'2024-11-20 06:37:00.000000','Team 1',9,2,24,19,11,8),(569,'2024-11-20 06:38:00.000000','Team 2',9,2,7,29,10,12),(570,'2024-11-20 06:39:00.000000','Team 1',12,24,20,27,11,8),(571,'2024-11-20 06:39:00.000000','Team 2',5,17,7,29,6,11),(572,'2024-11-20 06:40:00.000000','Team 1',12,24,7,29,11,6),(573,'2024-11-20 06:40:00.000000','Team 1',12,24,22,1,12,10),(574,'2024-11-20 06:43:00.000000','Team 2',12,24,2,9,8,11),(575,'2024-11-20 06:45:00.000000','Team 2',33,32,9,2,6,11),(576,'2024-11-20 06:50:00.000000','Team 2',29,7,2,9,8,11),(577,'2024-11-20 06:55:00.000000','Team 2',5,17,9,2,6,11),(578,'2024-11-20 06:57:00.000000','Team 1',20,27,9,2,12,10),(579,'2024-11-20 07:00:00.000000','Team 2',20,27,12,24,8,11),(580,'2024-11-22 06:15:00.000000','Team 1',1,18,2,29,11,9),(581,'2024-11-22 06:20:00.000000','Team 1',1,18,2,4,11,5),(582,'2024-11-22 06:27:00.000000','Team 1',1,18,12,9,11,6),(583,'2024-11-22 06:33:00.000000','Team 2',1,18,5,4,12,14),(584,'2024-11-22 06:40:00.000000','Team 2',12,22,5,4,11,13),(585,'2024-11-22 06:42:00.000000','Team 1',29,9,4,5,11,4),(586,'2024-11-22 06:45:00.000000','Team 2',29,9,11,2,5,11),(587,'2024-11-22 06:48:00.000000','Team 1',1,18,2,11,11,4),(588,'2024-11-22 06:53:00.000000','Team 2',1,18,12,22,5,11),(589,'2024-11-22 06:56:00.000000','Team 1',4,5,12,22,11,8),(590,'2024-11-22 06:59:00.000000','Team 1',4,5,29,9,11,9),(591,'2024-11-27 06:16:00.000000','Team 1',2,19,29,1,11,5),(592,'2024-11-27 06:22:00.000000','Team 1',2,19,13,24,11,7),(593,'2024-11-27 06:27:00.000000','Team 2',2,19,13,9,5,11),(594,'2024-11-27 06:34:00.000000','Team 2',12,24,13,9,9,11),(595,'2024-11-27 06:38:00.000000','Team 2',1,29,13,9,10,12),(596,'2024-11-27 06:42:00.000000','Team 1',19,2,13,9,11,9),(597,'2024-11-27 06:46:00.000000','Team 2',19,2,12,24,10,12),(598,'2024-11-27 06:50:00.000000','Team 1',29,1,12,24,11,6),(599,'2024-11-27 06:53:00.000000','Team 1',1,29,13,9,11,4),(600,'2024-11-27 06:56:00.000000','Team 1',1,29,12,24,11,5),(601,'2024-11-28 06:21:00.000000','Team 2',18,2,1,9,6,11),(602,'2024-11-28 06:28:00.000000','Team 2',17,29,9,1,9,11),(603,'2024-11-28 12:29:00.000000','Team 1',1,9,20,27,11,3),(604,'2024-11-28 06:35:00.000000','Team 1',18,2,9,1,11,6),(605,'2024-11-28 06:38:00.000000','Team 1',18,2,29,17,11,4),(606,'2024-11-28 06:41:00.000000','Team 1',18,2,20,27,11,4),(607,'2024-11-28 06:45:00.000000','Team 1',1,9,29,17,11,5),(608,'2024-11-28 06:48:00.000000','Team 1',1,9,27,20,11,5),(609,'2024-11-28 06:54:00.000000','Team 2',2,18,1,9,5,11),(610,'2024-11-28 06:58:00.000000','Team 2',18,29,1,9,6,11),(611,'2024-11-29 06:23:00.000000','Team 1',1,18,7,29,11,8),(612,'2024-11-29 06:24:00.000000','Team 2',17,9,1,18,9,11),(613,'2024-11-29 06:29:00.000000','Team 2',1,18,2,12,15,17),(614,'2024-11-29 06:39:00.000000','Team 1',12,2,7,29,11,6),(615,'2024-11-29 06:43:00.000000','Team 1',12,2,17,9,11,6),(616,'2024-11-29 06:46:00.000000','Team 2',2,12,1,18,5,11),(617,'2024-11-29 06:49:00.000000','Team 1',1,18,2,12,11,6),(618,'2024-11-29 06:52:00.000000','Team 1',18,1,7,29,11,8),(619,'2024-11-29 06:53:00.000000','Team 1',18,1,17,9,11,8),(620,'2024-11-29 07:00:00.000000','Team 2',12,2,1,18,5,11),(621,'2024-12-02 06:25:00.000000','Team 1',1,9,11,5,11,9),(622,'2024-12-02 06:30:00.000000','Team 2',1,9,12,29,5,11),(623,'2024-12-02 06:36:00.000000','Team 1',11,5,12,29,11,9),(624,'2024-12-02 06:39:00.000000','Team 2',11,5,29,9,10,12),(625,'2024-12-02 06:43:00.000000','Team 2',12,1,29,9,8,11),(626,'2024-12-02 06:47:00.000000','Team 2',11,5,29,9,11,13),(627,'2024-12-02 06:54:00.000000','Team 1',12,1,29,9,11,4),(628,'2024-12-02 06:54:00.000000','Team 2',12,1,11,5,9,11),(629,'2024-12-02 06:57:00.000000','Team 2',29,9,11,5,8,11),(630,'2024-12-04 06:19:00.000000','Team 2',19,2,22,1,6,11),(631,'2024-12-04 06:24:00.000000','Team 2',12,13,1,22,3,11),(632,'2024-12-04 06:29:00.000000','Team 2',9,29,1,22,6,11),(633,'2024-12-04 06:34:00.000000','Team 1',11,9,1,22,11,8),(634,'2024-12-04 06:38:00.000000','Team 2',11,9,2,19,12,14),(635,'2024-12-04 06:41:00.000000','Team 2',12,13,19,2,5,11),(636,'2024-12-04 06:46:00.000000','Team 1',29,9,19,2,13,11),(637,'2024-12-04 06:49:00.000000','Team 2',29,9,22,1,6,11),(638,'2024-12-04 06:53:00.000000','Team 2',11,9,22,1,11,13),(639,'2024-12-04 06:58:00.000000','Team 1',12,13,22,1,12,10),(640,'2024-12-06 06:18:00.000000','Team 1',22,1,7,14,11,6),(641,'2024-12-06 06:23:00.000000','Team 1',22,1,16,17,11,3),(642,'2024-12-06 06:32:00.000000','Team 2',22,1,9,12,7,11),(643,'2024-12-06 06:35:00.000000','Team 2',7,14,12,9,3,11),(644,'2024-12-06 06:37:00.000000','Team 2',17,16,12,9,4,11),(645,'2024-12-06 06:41:00.000000','Team 1',1,22,12,9,11,8),(646,'2024-12-06 06:44:00.000000','Team 1',1,22,7,14,11,4),(647,'2024-12-06 06:49:00.000000','Team 1',1,22,17,16,11,8),(648,'2024-12-06 06:53:00.000000','Team 2',22,1,12,9,9,11),(649,'2024-12-06 06:56:00.000000','Team 2',16,7,12,9,2,11),(650,'2024-12-10 06:21:00.000000','Team 1',22,1,17,7,11,6),(651,'2024-12-10 06:30:00.000000','Team 2',22,1,9,2,12,14),(652,'2024-12-10 06:35:00.000000','Team 1',12,29,7,17,11,4),(653,'2024-12-10 06:39:00.000000','Team 1',12,29,17,7,11,6),(654,'2024-12-10 06:44:00.000000','Team 1',12,29,22,1,15,13),(655,'2024-12-10 06:48:00.000000','Team 2',12,29,9,2,10,12),(656,'2024-12-10 06:49:00.000000','Team 2',5,8,9,2,6,11),(657,'2024-12-10 06:56:00.000000','Team 2',17,7,9,2,6,11),(658,'2024-12-12 06:20:00.000000','Team 2',1,7,29,18,12,14),(659,'2024-12-12 06:28:00.000000','Team 1',9,2,18,29,11,9),(660,'2024-12-12 06:33:00.000000','Team 1',9,2,5,1,11,3),(661,'2024-12-12 06:34:00.000000','Team 1',2,9,1,7,11,8),(662,'2024-12-12 06:37:00.000000','Team 2',2,9,12,17,8,11),(663,'2024-12-12 06:40:00.000000','Team 2',12,17,5,11,4,11),(664,'2024-12-12 06:43:00.000000','Team 1',11,5,19,29,11,4),(665,'2024-12-12 06:50:00.000000','Team 2',5,11,9,18,7,11),(666,'2024-12-12 06:54:00.000000','Team 2',1,7,18,9,10,12),(667,'2024-12-12 06:58:00.000000','Team 2',29,2,18,9,5,11);
/*!40000 ALTER TABLE "matches_doublesmatch" ENABLE KEYS */;
UN

--
-- Table structure for table "matches_singlesmatch"
--

DROP TABLE IF EXISTS "matches_singlesmatch";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "matches_singlesmatch" (
  "id" bigSERIAL PRIMARY KEY,
  "date" datetime(6) NOT NULL,
  "player1_id" bigint NOT NULL,
  "player2_id" bigint NOT NULL,
  "winner_id" bigint DEFAULT NULL,
  "player1_score" int NOT NULL,
  "player2_score" int NOT NULL,
  PRIMARY KEY ("id"),
  KEY "matches_singlesmatch_player1_id_8a60f7e0_fk_players_player_id" ("player1_id"),
  KEY "matches_singlesmatch_player2_id_6b5c74f2_fk_players_player_id" ("player2_id"),
  KEY "matches_singlesmatch_winner_id_66c6344e_fk_players_player_id" ("winner_id"),
  CONSTRAINT "matches_singlesmatch_player1_id_8a60f7e0_fk_players_player_id" FOREIGN KEY ("player1_id") REFERENCES "players_player" ("id"),
  CONSTRAINT "matches_singlesmatch_player2_id_6b5c74f2_fk_players_player_id" FOREIGN KEY ("player2_id") REFERENCES "players_player" ("id"),
  CONSTRAINT "matches_singlesmatch_winner_id_66c6344e_fk_players_player_id" FOREIGN KEY ("winner_id") REFERENCES "players_player" ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "matches_singlesmatch"
--


/*!40000 ALTER TABLE "matches_singlesmatch" DISABLE KEYS */;
INSERT INTO "matches_singlesmatch" VALUES (1,'2024-08-08 13:55:00.000000',18,23,18,11,7),(2,'2024-08-10 19:15:00.000000',18,9,18,11,9),(3,'2024-08-10 19:15:00.000000',12,18,12,11,9),(4,'2024-08-10 19:16:00.000000',12,5,12,11,9),(5,'2024-08-10 19:16:00.000000',12,9,12,11,2),(6,'2024-08-10 19:17:00.000000',4,18,4,11,5),(7,'2024-08-10 19:17:00.000000',4,12,4,15,13),(8,'2024-08-10 19:17:00.000000',4,9,4,11,6),(9,'2024-08-10 19:18:00.000000',4,5,4,11,4),(10,'2024-08-10 19:18:00.000000',4,12,12,5,11),(11,'2024-08-10 19:18:00.000000',12,18,12,11,6),(12,'2024-08-11 04:36:00.000000',1,15,1,11,9),(13,'2024-08-11 04:36:00.000000',1,15,1,13,11),(14,'2024-08-11 04:36:00.000000',1,15,15,10,12),(15,'2024-08-11 04:37:00.000000',1,15,15,7,11),(16,'2024-08-11 04:37:00.000000',15,1,15,11,6),(17,'2024-08-11 04:37:00.000000',15,1,15,12,10),(18,'2024-08-11 04:38:00.000000',1,15,15,9,11),(19,'2024-08-15 07:03:00.000000',12,13,12,11,0),(20,'2024-08-17 12:30:00.000000',15,8,15,11,9),(21,'2024-08-17 12:35:00.000000',15,5,15,11,9),(22,'2024-08-17 12:40:00.000000',15,1,15,11,6),(23,'2024-08-17 12:45:00.000000',15,8,15,11,6),(24,'2024-08-17 12:50:00.000000',15,1,15,11,9),(25,'2024-08-17 12:50:00.000000',15,5,15,11,7),(26,'2024-08-17 12:55:00.000000',15,8,8,9,11),(27,'2024-08-17 13:25:00.000000',5,15,15,11,13),(28,'2024-08-17 13:05:00.000000',15,5,5,9,11),(29,'2024-08-17 13:10:00.000000',5,8,5,11,6),(30,'2024-08-17 03:09:00.000000',5,15,15,12,14),(31,'2024-08-17 13:20:00.000000',15,8,8,6,11),(32,'2024-08-17 13:26:00.000000',5,8,5,12,10),(33,'2024-08-17 13:20:00.000000',8,15,15,11,13),(34,'2024-08-17 13:30:00.000000',15,5,15,11,5),(35,'2024-08-17 13:16:00.000000',15,8,8,7,11),(36,'2024-08-24 10:39:00.000000',18,9,18,11,9),(37,'2024-08-24 10:45:00.000000',18,9,18,11,4),(38,'2024-08-24 10:50:00.000000',18,9,18,11,6),(39,'2024-09-12 06:21:00.000000',1,19,1,11,6),(40,'2024-11-13 11:37:00.000000',18,1,18,11,7),(41,'2024-11-13 11:38:00.000000',18,11,18,12,10),(42,'2024-11-13 11:38:00.000000',22,1,1,8,11),(43,'2024-11-13 11:41:00.000000',18,8,18,11,7),(44,'2024-11-13 11:44:00.000000',18,22,18,11,5),(45,'2024-11-13 11:48:00.000000',18,1,18,11,6),(46,'2024-11-13 11:53:00.000000',18,11,11,10,12),(47,'2024-11-13 11:55:00.000000',8,11,11,4,11),(48,'2024-11-13 11:58:00.000000',22,11,11,5,11),(49,'2024-11-13 12:02:00.000000',1,11,11,5,11),(50,'2024-11-13 12:05:00.000000',18,11,11,6,11),(51,'2024-11-13 12:08:00.000000',8,11,11,5,11),(52,'2024-11-13 12:11:00.000000',22,11,11,6,11),(53,'2024-11-15 11:16:00.000000',18,1,18,11,7),(54,'2024-11-15 11:20:00.000000',18,11,18,11,8),(55,'2024-11-15 11:23:00.000000',2,11,11,3,11),(56,'2024-11-15 11:28:00.000000',12,11,12,11,9),(57,'2024-11-15 11:32:00.000000',12,16,12,11,3),(58,'2024-11-15 11:36:00.000000',12,1,12,11,8),(59,'2024-11-15 11:39:00.000000',12,18,12,11,6),(60,'2024-11-15 11:42:00.000000',12,2,12,11,5),(61,'2024-11-15 11:46:00.000000',12,11,11,10,12),(62,'2024-11-15 11:49:00.000000',22,11,11,4,11),(63,'2024-11-15 11:51:00.000000',8,11,11,3,11),(64,'2024-11-15 11:54:00.000000',36,11,11,7,11),(65,'2024-12-03 06:15:00.000000',7,2,2,9,11),(66,'2024-12-03 06:19:00.000000',1,2,2,4,11),(67,'2024-12-03 06:23:00.000000',22,2,2,6,11),(68,'2024-12-03 06:27:00.000000',9,2,2,8,11),(69,'2024-12-03 06:32:00.000000',12,2,12,11,6),(70,'2024-12-03 06:36:00.000000',12,7,12,11,4),(71,'2024-12-03 06:37:00.000000',12,1,12,11,1),(72,'2024-12-03 06:39:00.000000',12,22,12,11,1),(73,'2024-12-03 06:43:00.000000',12,9,12,11,6),(74,'2024-12-03 06:45:00.000000',12,2,12,11,2),(75,'2024-12-03 06:48:00.000000',12,7,12,11,4),(76,'2024-12-03 06:51:00.000000',12,1,12,11,6),(77,'2024-12-03 06:53:00.000000',12,22,12,11,4),(78,'2024-12-03 06:56:00.000000',12,9,12,11,4);
/*!40000 ALTER TABLE "matches_singlesmatch" ENABLE KEYS */;
UN

--
-- Table structure for table "players_player"
--

DROP TABLE IF EXISTS "players_player";
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE "players_player" (
  "id" bigSERIAL PRIMARY KEY,
  "first_name" varchar(100) NOT NULL,
  "last_name" varchar(100) NOT NULL,
  "date_of_birth" date DEFAULT NULL,
  "nationality" varchar(2) NOT NULL,
  "ranking" int NOT NULL,
  "photo" varchar(100) DEFAULT NULL,
  "alias" varchar(100) DEFAULT NULL,
  "gender" varchar(100) NOT NULL,
  "created_at" datetime(6) NOT NULL,
  "updated_at" datetime(6) NOT NULL,
  "matches_played" int NOT NULL,
  PRIMARY KEY ("id")
) 
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table "players_player"
--


/*!40000 ALTER TABLE "players_player" DISABLE KEYS */;
INSERT INTO "players_player" VALUES (1,'Juan','Sobalvarro','2004-08-23','NI',388,'player_photos/e648130a93924f388d133485ee1b9473.png','Developer','M','2024-08-06 02:52:52.780809','2024-12-12 18:55:14.090649',331),(2,'Rossman','Fuentes',NULL,'NI',170,'player_photos/3854e49923804427b6dc1bb5f601f725.png','Perrito','M','2024-08-06 03:08:06.468459','2024-12-12 18:58:15.836919',166),(4,'Aarón','Cisneros','1986-11-05','NI',122,'player_photos/a2195bc97819430d943d80f62e3c2bc5.png','Aarock','M','2024-08-06 15:18:19.320314','2024-11-22 18:59:18.389333',71),(5,'Ivania','Espinoza',NULL,'NI',92,'player_photos/73873eaaa7f54f248c410d06380237a1.jpg','Doc','F','2024-08-06 17:05:38.556732','2024-12-12 18:50:37.985859',153),(6,'Pablo','González',NULL,'NI',0,'player_photos/dd9288e9c7574ee19161793ca973aa48.jpg',NULL,'M','2024-08-06 17:16:36.048752','2024-08-11 07:17:19.206643',1),(7,'Steven','Mendoza',NULL,'NI',58,'player_photos/a99a920f7c8b4c6fb21b178ee20682eb.jpg','El Mewing','M','2024-08-06 17:40:02.997192','2024-12-12 18:55:14.284921',119),(8,'Christian','Toval',NULL,'NI',68,'player_photos/b97236a0e7fe4d8e95e2f05abb855d33.jpg','Machete','M','2024-08-06 17:43:28.227566','2024-12-10 18:53:10.762969',94),(9,'Leonardo','Bojorge',NULL,'NI',350,'player_photos/014d66de9021461eafe3b20a5280654b.jpg','Leo','M','2024-08-06 17:44:24.723861','2024-12-12 18:58:16.476905',289),(10,'Leticia','Bermejo',NULL,'NI',0,'player_photos/92dd2a1283774b99aaa38fe42e77483c.png','Leti','F','2024-08-06 17:45:13.439929','2024-08-11 07:17:34.309943',1),(11,'Abraham','Miranda','1996-08-01','NI',264,'player_photos/7233159f84ae470a837e3df6010bcef7.jpg',NULL,'M','2024-08-06 17:46:30.142764','2024-12-12 18:50:38.154320',187),(12,'Alfredo','Martínez',NULL,'NI',382,'player_photos/daeb2382cdaa40d599d784ab4991a117.jpg',NULL,'M','2024-08-06 17:47:01.672477','2024-12-12 18:43:19.021013',274),(13,'Andrés','Molina',NULL,'HN',54,'player_photos/66fda1ece7d74af6891351d3c73da1fd.jpg','Corcobero','M','2024-08-06 17:47:49.108507','2024-12-04 19:02:36.792561',49),(14,'Jeremy','Chávez',NULL,'NI',2,'player_photos/562fecb3861048dcaaefc39c294ff103.jpg','Don Señor Don','M','2024-08-06 17:49:18.019458','2024-12-06 18:44:10.669952',32),(15,'Heyner','Núñez',NULL,'NI',154,'player_photos/1251189ed57246699980df575267d106.jpg','El primo','M','2024-08-06 17:50:20.050099','2024-11-15 18:52:10.388495',158),(16,'Ari','Castillo','2004-09-30','US',6,'player_photos/86bd697f5f8f4ea7ad5d6d5ce78eb106.png','Desaparecido','M','2024-08-06 17:56:37.503417','2024-12-06 18:56:59.449023',12),(17,'Adilia','Moreno','2005-03-30','KR',4,'player_photos/1fe63bc690d242c68ade2f5c82ba666f.png','Quesillolover','F','2024-08-06 18:01:03.102998','2024-12-12 18:43:19.205340',48),(18,'Lester','Munguía',NULL,'NI',268,'player_photos/ae2653366deb4beeb1d3d8e79fdac339.png','La Bestia','M','2024-08-06 18:31:57.468051','2024-12-12 18:58:16.367761',241),(19,'Bismarck','González',NULL,'NI',28,'player_photos/cd34844a4f6246fab425defee7ce9230.jpg',NULL,'M','2024-08-06 18:55:28.037609','2024-12-12 18:46:31.595951',67),(20,'Alejandro','Silva',NULL,'NI',16,'player_photos/97e64b7c21654c05b6cbdf324b84015f.jpg',NULL,'M','2024-08-06 18:56:13.745320','2024-12-03 18:36:26.700412',47),(21,'Andrea','-',NULL,'NI',0,'player_photos/e40a7a78c4174a0cbbf8bf30667b677e.jpeg','La prima','','2024-08-07 03:01:04.158044','2024-08-20 14:17:06.947040',11),(22,'Esther','Martínez','2005-02-12','NI',78,'player_photos/be4877be73c84d10b77aa3f3863c0299.png','Estrés','F','2024-08-07 03:14:36.950483','2024-12-10 18:44:59.244630',92),(23,'Omar','Lara','1986-12-22','NI',22,'player_photos/6da286668bd441d786b79d41dcda8a4d.jpeg','El buen hombre','','2024-08-07 14:24:31.805442','2024-08-26 22:33:26.787098',24),(24,'Penélope','Martínez',NULL,'NI',58,'player_photos/17a9a943a95a4f5592c22b16f4e25319.png','Pepe','F','2024-08-07 18:27:25.783127','2024-11-27 18:57:13.225877',65),(25,'Andry','Madrigales',NULL,'NI',10,'player_photos/e22d06a0ae82430fa9f7766084ea1691.jpg',NULL,'M','2024-08-08 18:33:23.698403','2024-11-13 19:11:06.737897',19),(26,'Juan','Baltodano',NULL,'NI',8,'player_photos/c8e2f545f4c0451b884a534f35649035.jpg',NULL,'M','2024-08-08 18:34:17.079997','2024-11-19 18:34:04.702145',7),(27,'Jehonatan','Ayala',NULL,'NI',14,'player_photos/9c8da08a93ad449185bd84ba82416eeb.jpg',NULL,'','2024-08-08 18:35:13.104750','2024-11-28 18:51:22.039871',35),(28,'Nelson','Mayorga',NULL,'NI',32,'player_photos/0173d7983ab04d11bb936af1c078d988.jpeg','El matador','','2024-08-10 13:55:10.304044','2024-08-26 22:35:55.179622',25),(29,'Jadan','Robateau','2005-02-25','NI',64,'player_photos/28957d56971e4575b9b930d6357e1b47.jpg',NULL,'M','2024-08-13 02:40:51.790377','2024-12-12 18:58:15.656001',89),(30,'Ernesto','Torrez','2004-01-20','NI',2,'player_photos/5cd3d9c8d72347fd882f2bdc303c7782.jpg','Kingdred','M','2024-08-14 21:50:21.170759','2024-11-07 18:38:45.689754',7),(31,'Cinthia Del Carmen','Granera García','1989-05-12','NI',48,'',NULL,'F','2024-09-10 18:20:45.426512','2024-09-27 19:56:48.886907',35),(32,'Marcelo','Tercero','2005-06-10','NI',2,'',NULL,'M','2024-11-07 18:19:10.075220','2024-11-20 18:46:18.673324',11),(33,'Ahsley','Robelo','2005-03-21','NI',4,'player_photos/64350aca7d8c44f7ab8ce677458a6f55.jpg','Cuervo','M','2024-11-13 23:50:06.790337','2024-11-20 18:46:18.665692',5),(34,'Miguel','Morales','2007-02-05','NI',0,'','El Negro','M','2024-11-14 18:38:36.543226','2024-11-14 18:41:02.746050',1),(35,'Rogelio','Selva','2002-05-31','NI',0,'','Selva','M','2024-11-14 18:46:27.693924','2024-11-14 18:49:15.865031',1),(36,'Mariam','Vanegas','1998-04-23','NI',4,'',NULL,'F','2024-11-15 23:52:27.353778','2024-11-16 01:03:15.379371',9);
/*!40000 ALTER TABLE "players_player" ENABLE KEYS */;
UN
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-01-16 18:08:38
