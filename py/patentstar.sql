/*
MySQL

Source Server         : windows2008
Source Server Version : 50627
Source Host           : 127.0.0.1:3306
Source Database       : patent

Target Server Type    : MYSQL
Target Server Version : 50627
File Encoding         : 65001

Date: 2016-06-05 20:31:52
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for patentstar
-- ----------------------------
DROP TABLE IF EXISTS `patentstar`;
CREATE TABLE `patentstar` (
  `StrSerialNo` varchar(255) NOT NULL,
  `StrANX` varchar(255) DEFAULT NULL,
  `StrApNo` varchar(255) DEFAULT NULL,
  `StrApDate` varchar(255) DEFAULT NULL,
  `StrPubNo` varchar(255) DEFAULT NULL,
  `StrPubDate` varchar(255) DEFAULT NULL,
  `StrAnnNo` varchar(255) DEFAULT NULL,
  `StrAnnDate` varchar(255) DEFAULT NULL,
  `StrPnOrGn` varchar(255) DEFAULT NULL,
  `StrPdOrGd` varchar(255) DEFAULT NULL,
  `StrMainIPC` varchar(255) DEFAULT NULL,
  `StrIpc` text,
  `StrPri` varchar(255) DEFAULT NULL,
  `StrInventor` varchar(255) DEFAULT NULL,
  `StrApply` varchar(255) DEFAULT NULL,
  `StrTitle` varchar(255) DEFAULT NULL,
  `StrFiled` varchar(255) DEFAULT NULL,
  `StrCountryCode` varchar(255) DEFAULT NULL,
  `StrAgency` varchar(255) DEFAULT NULL,
  `StrAgency_Addres` varchar(255) DEFAULT NULL,
  `StrClaim` text,
  `StrAbstr` text,
  `StrFtUrl` varchar(255) DEFAULT NULL,
  `CPIC` varchar(255) DEFAULT NULL,
  `Brief` varchar(255) DEFAULT NULL,
  `TongZu` varchar(255) DEFAULT NULL,
  `ZhuanLiLeiXing` varchar(255) DEFAULT NULL,
  `FaLvZhuangTai` varchar(255) DEFAULT NULL,
  `StrShenQingRenDiZhi` varchar(255) DEFAULT NULL,
  `StrDaiLiRen` varchar(255) DEFAULT NULL,
  `Form` varchar(255) DEFAULT NULL,
  `Iscore` varchar(255) DEFAULT NULL,
  `Note` varchar(255) DEFAULT NULL,
  `NoteDate` varchar(255) DEFAULT NULL,
  `StrDocdbApNo` varchar(255) DEFAULT NULL,
  `StrEpoApNo` varchar(255) DEFAULT NULL,
  `StrOriginalApNo` varchar(255) DEFAULT NULL,
  `StrDocdbPubNo` varchar(255) DEFAULT NULL,
  `StrEpoPubNo` varchar(255) DEFAULT NULL,
  `StrOriginalPubNo` varchar(255) DEFAULT NULL,
  `StrAbsFmy` varchar(255) DEFAULT NULL,
  `StrRefDoc` varchar(255) DEFAULT NULL,
  `StrEcla` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`StrSerialNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
