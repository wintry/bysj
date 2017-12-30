/*
 Navicat Premium Data Transfer

 Source Server         : bysj
 Source Server Type    : PostgreSQL
 Source Server Version : 90510
 Source Host           : localhost:5432
 Source Catalog        : bysj
 Source Schema         : public

 Target Server Type    : PostgreSQL
 Target Server Version : 90510
 File Encoding         : 65001

 Date: 30/12/2017 17:58:05
*/


-- ----------------------------
-- Sequence structure for bugs_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."bugs_id_seq";
CREATE SEQUENCE "public"."bugs_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for logs_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."logs_id_seq";
CREATE SEQUENCE "public"."logs_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for product_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."product_id_seq";
CREATE SEQUENCE "public"."product_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Sequence structure for user_id_seq
-- ----------------------------
DROP SEQUENCE IF EXISTS "public"."user_id_seq";
CREATE SEQUENCE "public"."user_id_seq" 
INCREMENT 1
MINVALUE  1
MAXVALUE 9223372036854775807
START 1
CACHE 1;

-- ----------------------------
-- Table structure for bugs
-- ----------------------------
DROP TABLE IF EXISTS "public"."bugs";
CREATE TABLE "public"."bugs" (
  "id" int4 NOT NULL DEFAULT nextval('bugs_id_seq'::regclass),
  "title" varchar(200) COLLATE "pg_catalog"."default",
  "detail" varchar(200) COLLATE "pg_catalog"."default",
  "img" varchar(200) COLLATE "pg_catalog"."default",
  "product_id" int4,
  "line_id" int4,
  "create_time" varchar(200) COLLATE "pg_catalog"."default",
  "user_id" int4
)
;

-- ----------------------------
-- Table structure for logs
-- ----------------------------
DROP TABLE IF EXISTS "public"."logs";
CREATE TABLE "public"."logs" (
  "id" int4 NOT NULL DEFAULT nextval('logs_id_seq'::regclass),
  "content" varchar(100) COLLATE "pg_catalog"."default",
  "user_id" int4,
  "create_time" varchar(20) COLLATE "pg_catalog"."default"
)
;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS "public"."product";
CREATE TABLE "public"."product" (
  "id" int4 NOT NULL DEFAULT nextval('product_id_seq'::regclass),
  "name" varchar(50) COLLATE "pg_catalog"."default",
  "fid" int4
)
;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS "public"."user";
CREATE TABLE "public"."user" (
  "id" int4 NOT NULL DEFAULT nextval('user_id_seq'::regclass),
  "username" varchar(10) COLLATE "pg_catalog"."default" NOT NULL,
  "pwd" varchar(50) COLLATE "pg_catalog"."default" NOT NULL,
  "phone" varchar(11) COLLATE "pg_catalog"."default" NOT NULL,
  "token" varchar(50) COLLATE "pg_catalog"."default",
  "lv" int4
)
;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO "public"."user" VALUES (2, 'yjg', '08f8e0260c64418510cefb2b06eee5cd', '18777777777', NULL, 1);
INSERT INTO "public"."user" VALUES (3, 'yjg1', '08f8e0260c64418510cefb2b06eee5cd', '18777777777', NULL, 2);
INSERT INTO "public"."user" VALUES (1, 'xuyh', '47bce5c74f589f4867dbd57e9ca9f808', '13766666666', '20d3c632b21040ed95dfe8a1756cce7f', 3);

-- ----------------------------
-- Alter sequences owned by
-- ----------------------------
ALTER SEQUENCE "public"."bugs_id_seq"
OWNED BY "public"."bugs"."id";
SELECT setval('"public"."bugs_id_seq"', 2, true);
ALTER SEQUENCE "public"."logs_id_seq"
OWNED BY "public"."logs"."id";
SELECT setval('"public"."logs_id_seq"', 2, true);
ALTER SEQUENCE "public"."product_id_seq"
OWNED BY "public"."product"."id";
SELECT setval('"public"."product_id_seq"', 3, true);
ALTER SEQUENCE "public"."user_id_seq"
OWNED BY "public"."user"."id";
SELECT setval('"public"."user_id_seq"', 4, true);

-- ----------------------------
-- Primary Key structure for table bugs
-- ----------------------------
ALTER TABLE "public"."bugs" ADD CONSTRAINT "bugs_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table logs
-- ----------------------------
ALTER TABLE "public"."logs" ADD CONSTRAINT "logs_pkey" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table product
-- ----------------------------
ALTER TABLE "public"."product" ADD CONSTRAINT "product_id_pk" PRIMARY KEY ("id");

-- ----------------------------
-- Primary Key structure for table user
-- ----------------------------
ALTER TABLE "public"."user" ADD CONSTRAINT "user_id_pk" PRIMARY KEY ("id");
