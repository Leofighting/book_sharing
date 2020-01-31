/*
 Navicat Premium Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 80012
 Source Host           : localhost:3306
 Source Schema         : fisher_new

 Target Server Type    : MySQL
 Target Server Version : 80012
 File Encoding         : 65001

 Date: 31/01/2020 22:02:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book
-- ----------------------------
DROP TABLE IF EXISTS `book`;
CREATE TABLE `book`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `author` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `binding` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `publisher` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `price` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pages` int(11) DEFAULT NULL,
  `pubdate` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `isbn` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `summary` varchar(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `image` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `isbn`(`isbn`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for drift
-- ----------------------------
DROP TABLE IF EXISTS `drift`;
CREATE TABLE `drift`  (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `recipient_name` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `message` varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `mobile` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `isbn` varchar(13) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `book_title` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `book_author` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `book_img` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `requester_id` int(11) DEFAULT NULL,
  `requester_nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `gifter_id` int(11) DEFAULT NULL,
  `gift_id` int(11) DEFAULT NULL,
  `gifter_nickname` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pending` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of drift
-- ----------------------------
INSERT INTO `drift` VALUES (1580353405, 1, 1, 'tom', '广州市白云区xx*******', '', '13322222222', '9787544247269', '1Q84 BOOK 1', '[日]村上春树', 'https://img3.doubanio.com/lpic/s4363464.jpg', 3, 'tom', 3, 3, 'jack', 1);

-- ----------------------------
-- Table structure for gift
-- ----------------------------
DROP TABLE IF EXISTS `gift`;
CREATE TABLE `gift`  (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `isbn` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `launched` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uid`(`uid`) USING BTREE,
  CONSTRAINT `gift_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 5 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of gift
-- ----------------------------
INSERT INTO `gift` VALUES (1580286392, 1, 1, 3, '9787807240648', 0);
INSERT INTO `gift` VALUES (1580303427, 1, 2, 2, '9787506320511', 0);
INSERT INTO `gift` VALUES (1580353246, 1, 3, 3, '9787544247269', 0);
INSERT INTO `gift` VALUES (1580353310, 1, 4, 2, '9787532725694', 0);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `nickname` varchar(24) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `phone_number` varchar(18) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `confirmed` tinyint(1) DEFAULT NULL,
  `beans` float DEFAULT NULL,
  `send_counter` int(11) DEFAULT NULL,
  `receive_counter` int(11) DEFAULT NULL,
  `wx_open_id` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `wx_name` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE INDEX `email`(`email`) USING BTREE,
  UNIQUE INDEX `phone_number`(`phone_number`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (NULL, 1, 1, 'pbkdf2:sha256:150000$PnfFiK1i$fad79dfbb854ca5e075db259f7dccd36bbadaddef2b92e0cad89f1076f3929cc', 'leo', NULL, 'leo@163.com', 0, 0, 0, 0, NULL, NULL);
INSERT INTO `user` VALUES (1579595379, 1, 2, 'pbkdf2:sha256:150000$DWKZx4pV$2ec66c69e57f25f126557878f93d554c291e0a6cf7af94fcb686cd53a047971e', 'tom', NULL, 'tom@163.com', 0, 0, 0, 0, NULL, NULL);
INSERT INTO `user` VALUES (1580266540, 1, 3, 'pbkdf2:sha256:150000$Eesuefwa$b6484be793122bd10cccdac582114fec965f81a455b4f9145811040b8aa2aa83', 'jack', NULL, 'jack@qq.com', 0, 1, 0, 0, NULL, NULL);

-- ----------------------------
-- Table structure for wish
-- ----------------------------
DROP TABLE IF EXISTS `wish`;
CREATE TABLE `wish`  (
  `create_time` int(11) DEFAULT NULL,
  `status` smallint(6) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) DEFAULT NULL,
  `isbn` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `launched` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `uid`(`uid`) USING BTREE,
  CONSTRAINT `wish_ibfk_1` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wish
-- ----------------------------
INSERT INTO `wish` VALUES (1580288142, 1, 1, 3, '9787506320511', 0);
INSERT INTO `wish` VALUES (1580299797, 1, 2, 2, '9787807240648', 0);
INSERT INTO `wish` VALUES (1580303471, 1, 3, 2, '9787500831112', 0);
INSERT INTO `wish` VALUES (1580353227, 1, 4, 3, '9787532725694', 0);
INSERT INTO `wish` VALUES (1580353272, 1, 5, 3, '9787532730001', 0);
INSERT INTO `wish` VALUES (1580353324, 1, 6, 2, '9787544247269', 0);

SET FOREIGN_KEY_CHECKS = 1;
