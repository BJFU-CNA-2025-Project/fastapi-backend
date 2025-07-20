CREATE TABLE `user_activity` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  `status` varchar(20) DEFAULT NULL COMMENT '活动状态',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `user_activity_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_activity_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户关联活动表'

CREATE TABLE `star_activities` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `star_activities_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `star_activities_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户收藏活动表'

CREATE TABLE `activities` (
  `activity_id` int NOT NULL AUTO_INCREMENT COMMENT '活动ID(PK)',
  `title` varchar(30) DEFAULT NULL COMMENT '标题',
  `date` date DEFAULT NULL COMMENT '活动日期',
  `location` varchar(60) DEFAULT NULL COMMENT '活动地点',
  `calorie` int DEFAULT NULL COMMENT '消耗卡路里',
  `duration` int DEFAULT NULL COMMENT '时长(分钟)',
  `weather` int DEFAULT NULL COMMENT '天气',
  `start_place` varchar(60) DEFAULT NULL COMMENT '起点',
  `end_place` varchar(60) DEFAULT NULL COMMENT '终点',
  `time` time DEFAULT NULL COMMENT '活动时间',
  `difficulty` varchar(10) DEFAULT NULL COMMENT '难度',
  `type` varchar(15) DEFAULT NULL COMMENT '活动类型',
  `image` varchar(150) DEFAULT NULL COMMENT '活动图片URL',
  `star_count` int DEFAULT NULL,
  PRIMARY KEY (`activity_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='活动表'

CREATE TABLE `blog_label` (
  `label_id` int NOT NULL COMMENT '标签ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`label_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `blog_label_ibfk_1` FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT `blog_label_ibfk_2` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='帖子拥有标签表'

CREATE TABLE `topic_blog` (
  `topic_id` int NOT NULL COMMENT '话题ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`topic_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `topic_blog_ibfk_1` FOREIGN KEY (`topic_id`) REFERENCES `topic` (`topic_id`) ON DELETE CASCADE,
  CONSTRAINT `topic_blog_ibfk_2` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='话题关联帖子表'

CREATE TABLE `labels` (
  `label_id` int NOT NULL AUTO_INCREMENT COMMENT '标签ID(PK)',
  `content` varchar(30) DEFAULT NULL COMMENT '内容',
  PRIMARY KEY (`label_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='标签表'

CREATE TABLE `topic` (
  `topic_id` int NOT NULL AUTO_INCREMENT COMMENT '话题ID(PK)',
  `title` varchar(50) DEFAULT NULL COMMENT '标题',
  `description` varchar(255) DEFAULT NULL COMMENT '话题描述',
  `color` varchar(20) DEFAULT NULL COMMENT '主题色',
  `icon` varchar(150) DEFAULT NULL COMMENT '图标',
  `image` varchar(150) DEFAULT NULL COMMENT '封面图片',
  PRIMARY KEY (`topic_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='话题表'

CREATE TABLE `exercise_data` (
  `exercise_id` int NOT NULL AUTO_INCREMENT COMMENT '运动数据ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `time` datetime DEFAULT NULL COMMENT '天数',
  `step` int DEFAULT NULL COMMENT '运动步数',
  PRIMARY KEY (`exercise_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `exercise_data_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='运动数据表'

CREATE TABLE `enroll` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  `enroll_time` datetime DEFAULT NULL COMMENT '报名时间',
  PRIMARY KEY (`user_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `enroll_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `enroll_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户报名活动表'

CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '帖子ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '评论内容',
  `commentTime` datetime DEFAULT NULL COMMENT '评论时间',
  PRIMARY KEY (`comment_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='评论表'

CREATE TABLE `blogs` (
  `blog_id` int NOT NULL AUTO_INCREMENT COMMENT '帖子ID(PK)',
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `activity_id` int DEFAULT NULL COMMENT '活动ID(FK)',
  `post_time` datetime DEFAULT NULL COMMENT '发送时间',
  `title` varchar(50) DEFAULT NULL COMMENT '标题',
  `content` varchar(1024) DEFAULT NULL COMMENT '内容',
  `like_count` int DEFAULT NULL COMMENT '点赞数',
  `star_count` int DEFAULT NULL COMMENT '收藏数量',
  PRIMARY KEY (`blog_id`),
  KEY `activity_id` (`activity_id`),
  KEY `blogs_ibfk_1` (`user_id`),
  CONSTRAINT `blogs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `blogs_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='帖子表'

CREATE TABLE `activity_label` (
  `label_id` int NOT NULL COMMENT '标签ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`label_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `activity_label_ibfk_1` FOREIGN KEY (`label_id`) REFERENCES `labels` (`label_id`) ON DELETE CASCADE,
  CONSTRAINT `activity_label_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='活动拥有标签表'

CREATE TABLE `blog_activity` (
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  `activity_id` int NOT NULL COMMENT '活动ID(FK)',
  PRIMARY KEY (`blog_id`,`activity_id`),
  KEY `activity_id` (`activity_id`),
  CONSTRAINT `blog_activity_ibfk_1` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE,
  CONSTRAINT `blog_activity_ibfk_2` FOREIGN KEY (`activity_id`) REFERENCES `activities` (`activity_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='帖子关联活动表'

CREATE TABLE `user_like_blog` (
  `like_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL COMMENT '用户ID(FK)',
  `blog_id` int DEFAULT NULL COMMENT '帖子ID(FK)',
  `content` varchar(255) DEFAULT NULL COMMENT '评论内容',
  PRIMARY KEY (`like_id`),
  KEY `user_id` (`user_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `user_like_blog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_like_blog_ibfk_2` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='评论表'

CREATE TABLE `user_star_blogs` (
  `user_id` int NOT NULL COMMENT '用户ID(FK)',
  `blog_id` int NOT NULL COMMENT '帖子ID(FK)',
  PRIMARY KEY (`user_id`,`blog_id`),
  KEY `blog_id` (`blog_id`),
  CONSTRAINT `user_star_blogs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `user_star_blogs_ibfk_2` FOREIGN KEY (`blog_id`) REFERENCES `blogs` (`blog_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户收藏帖子表'

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT COMMENT '用户ID(PK)',
  `name` varchar(20) DEFAULT NULL COMMENT '用户昵称',
  `avatar` varchar(100) DEFAULT NULL COMMENT '头像URL',
  `level` int DEFAULT NULL COMMENT '用户等级',
  `points` int DEFAULT NULL COMMENT '积分数量',
  `days` int DEFAULT NULL COMMENT '连续打卡数',
  `phone_number` varchar(20) DEFAULT NULL COMMENT '手机号',
  `register_time` datetime DEFAULT NULL COMMENT '注册时间',
  `account` varchar(20) DEFAULT NULL COMMENT '账号',
  `password` varchar(20) DEFAULT NULL COMMENT '密码',
  `open_id` varchar(30) DEFAULT NULL COMMENT '微信openId',
  `union_id` varchar(30) DEFAULT NULL COMMENT '微信unionId',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='用户表'

