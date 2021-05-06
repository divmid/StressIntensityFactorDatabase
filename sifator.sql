/*
SQLyog Ultimate v10.00 Beta1
MySQL - 5.7.28-log : Database - sifator
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`sifator` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `sifator`;

/*Table structure for table `sifable2` */

DROP TABLE IF EXISTS `sifable2`;

CREATE TABLE `sifable2` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable2` */

insert  into `sifable2`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.002),(0.15,1.004),(0.20,1.009),(0.25,1.022),(0.30,1.032),(0.35,1.054),(0.40,1.072),(0.45,1.108),(0.50,1.130),(0.55,1.635),(0.60,1.195),(0.65,1.265),(0.70,1.330),(0.75,1.433),(0.80,1.530),(0.85,1.704),(0.90,1.937);

/*Table structure for table `sifable3` */

DROP TABLE IF EXISTS `sifable3`;

CREATE TABLE `sifable3` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable3` */

insert  into `sifable3`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.004),(0.15,1.007),(0.20,1.014),(0.25,1.022),(0.30,1.042),(0.35,1.063),(0.40,1.081),(0.45,1.114),(0.50,1.136),(0.55,1.178),(0.60,1.221),(0.65,1.294),(0.70,1.357),(0.75,1.447),(0.80,1.578),(0.85,1.765),(0.90,2.018),(0.90,2.018);

/*Table structure for table `sifable4` */

DROP TABLE IF EXISTS `sifable4`;

CREATE TABLE `sifable4` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable4` */

insert  into `sifable4`(`q`,`f`) values (0.00,1.001),(0.05,1.004),(0.10,1.009),(0.15,1.015),(0.20,1.023),(0.25,1.036),(0.30,1.050),(0.35,1.069),(0.40,1.097),(0.45,1.130),(0.50,1.153),(0.55,1.195),(0.60,1.237),(0.65,1.308),(0.70,1.388),(0.75,1.503),(0.80,1.630),(0.85,1.859),(0.90,2.170);

/*Table structure for table `sifable5` */

DROP TABLE IF EXISTS `sifable5`;

CREATE TABLE `sifable5` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable5` */

insert  into `sifable5`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.002),(0.15,1.003),(0.20,1.011),(0.25,1.020),(0.30,1.029),(0.35,1.053),(0.40,1.076),(0.45,1.105),(0.50,1.127),(0.55,1.167),(0.60,1.203),(0.65,1.369),(0.70,1.328),(0.75,1.430),(0.80,1.532),(0.85,1.724),(0.90,1.936);

/*Table structure for table `sifable6` */

DROP TABLE IF EXISTS `sifable6`;

CREATE TABLE `sifable6` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable6` */

insert  into `sifable6`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.002),(0.15,1.009),(0.20,1.014),(0.25,1.027),(0.30,1.037),(0.35,1.067),(0.40,1.086),(0.45,1.113),(0.50,1.138),(0.55,1.181),(0.60,1.221),(0.65,1.289),(0.70,1.355),(0.75,1.449),(0.80,1.568),(0.85,1.783),(0.90,2.012);

/*Table structure for table `sifable7` */

DROP TABLE IF EXISTS `sifable7`;

CREATE TABLE `sifable7` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable7` */

insert  into `sifable7`(`q`,`f`) values (0.00,1.001),(0.05,1.004),(0.10,1.006),(0.15,1.011),(0.20,1.017),(0.25,1.022),(0.30,1.030),(0.35,1.047),(0.40,1.061),(0.45,1.085),(0.50,1.110),(0.55,1.148),(0.60,1.180),(0.65,1.240),(0.70,1.292),(0.75,1.392),(0.80,1.485),(0.85,1.637),(0.90,1.856);

/*Table structure for table `sifable8` */

DROP TABLE IF EXISTS `sifable8`;

CREATE TABLE `sifable8` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable8` */

insert  into `sifable8`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.004),(0.15,1.006),(0.20,1.007),(0.25,1.014),(0.30,1.022),(0.35,1.032),(0.40,1.045),(0.45,1.060),(0.50,1.075),(0.55,1.101),(0.60,1.124),(0.65,1.157),(0.70,1.193),(0.75,1.247),(0.80,1.315),(0.85,1.422),(0.90,1.564);

/*Table structure for table `sifable9` */

DROP TABLE IF EXISTS `sifable9`;

CREATE TABLE `sifable9` (
  `q` double(3,2) DEFAULT NULL,
  `f` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sifable9` */

insert  into `sifable9`(`q`,`f`) values (0.00,1.000),(0.05,1.001),(0.10,1.004),(0.15,1.011),(0.20,1.017),(0.25,1.022),(0.30,1.030),(0.35,1.045),(0.40,1.056),(0.45,1.075),(0.50,1.092),(0.55,1.126),(0.60,1.152),(0.65,1.197),(0.70,1.241),(0.75,1.319),(0.80,1.399),(0.85,1.545),(0.90,1.709);

/*Table structure for table `siftable` */

DROP TABLE IF EXISTS `siftable`;

CREATE TABLE `siftable` (
  `k` double(3,2) DEFAULT NULL,
  `F` double(4,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `siftable` */

insert  into `siftable`(`k`,`F`) values (0.00,1.000),(0.05,1.012),(0.10,1.023),(0.15,1.030),(0.20,1.033),(0.25,1.042),(0.30,1.051),(0.35,1.072),(0.40,1.088),(0.50,1.152),(0.55,1.212),(0.60,1.243),(0.65,1.332),(0.70,1.384),(0.75,1.486),(0.85,1.867),(0.90,2.178),(0.95,2.278);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
