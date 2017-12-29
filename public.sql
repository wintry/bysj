/*
 Navicat Premium Data Transfer

 Source Server         : localhost_2345
 Source Server Type    : PostgreSQL
 Source Server Version : 90604
 Source Host           : localhost:2345
 Source Catalog        : crazyrebate
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90604
 File Encoding         : 65001

 Date: 23/08/2017 16:24:13
*/


-- ----------------------------
-- Sequence structure for sort_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."sort_id_seq";
CREATE SEQUENCE "public"."sort_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for share
-- ----------------------------
DROP TABLE IF EXISTS "public"."share";
CREATE TABLE "public"."share" (
  "id" uuid NOT NULL DEFAULT NULL,
  "title" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "content" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "url" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "click amount" int4 DEFAULT NULL,
  "view_quantity" int4 DEFAULT NULL,
  "r_id" uuid DEFAULT NULL,
  "create_time" timestamp(0) DEFAULT NULL,
  "tag" json DEFAULT NULL,
  "sort" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "score" float4 DEFAULT NULL,
  "price" float4 DEFAULT NULL,
  "img" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for sort
-- ----------------------------
DROP TABLE IF EXISTS "public"."sort";
CREATE TABLE "public"."sort" (
  "id" int4 NOT NULL DEFAULT nextval('sort_id_seq'::regclass),
  "pid" int4 DEFAULT NULL,
  "name" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL
)
;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" uuid NOT NULL DEFAULT NULL,
  "phone" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "nickname" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "pwd" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "create_time" timestamp(6) DEFAULT NULL::timestamp without time zone,
  "share_stars" int4 DEFAULT NULL,
  "share_click" int4 DEFAULT NULL,
  "evaluation" int2 DEFAULT NULL,
  "sex" bool DEFAULT NULL,
  "avater" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "star" uuid[] DEFAULT NULL
)
;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "public"."user" VALUES ('3b3adfd0-72a4-4e19-b192-b7272bcb8af5', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."user" VALUES ('3b3adfd0-72a4-4e19-b192-b7272bcb8af7', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);
INSERT INTO "public"."user" VALUES ('3b3adfd0-72a4-4e19-b192-b7272bcb8af6', '18758290214', NULL, 'ad57484016654da87125db86f4227ea3', NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- ----------------------------
-- Table structure for user_share
-- ----------------------------
DROP TABLE IF EXISTS "public"."user_share";
CREATE TABLE "public"."user_share" (
  "id" uuid NOT NULL DEFAULT NULL,
  "user_id" int4 DEFAULT NULL,
  "share_id" int4 DEFAULT NULL,
  "score" int2 DEFAULT NULL,
  "content" varchar(255) COLLATE "pg_catalog"."default" DEFAULT NULL,
  "is_bought" bool DEFAULT NULL
)
;

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."sort_id_seq"
OWNED BY "public"."sort"."id";
SELECT setval('"public"."sort_id_seq"', 2, false);

-- ----------------------------
-- Primary Key structure for table share
-- ----------------------------
ALTER TABLE "public"."share" ADD CONSTRAINT "share_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table sort
-- ----------------------------
ALTER TABLE "public"."sort" ADD CONSTRAINT "sort_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user_share
-- ----------------------------
ALTER TABLE "public"."user_share" ADD CONSTRAINT "user_share_pkey" PRIMARY KEY ("id");
