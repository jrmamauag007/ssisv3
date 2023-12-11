
DROP TABLE IF EXISTS Students;
DROP TABLE IF EXISTS Courses;
DROP TABLE IF EXISTS Colleges;


CREATE TABLE Colleges (
    collegecode VARCHAR(50) PRIMARY KEY NOT NULL,
    collegename VARCHAR(255) DEFAULT NULL
);


CREATE TABLE Courses (
    coursecode VARCHAR(50) PRIMARY KEY NOT NULL,
    coursename VARCHAR(255) DEFAULT NULL,
    collegecode VARCHAR(50) NOT NULL,
    FOREIGN KEY (collegecode) REFERENCES Colleges(collegecode) ON DELETE CASCADE
);

CREATE TABLE Students (
    id VARCHAR(50) PRIMARY KEY NOT NULL,
    firstname VARCHAR(255) DEFAULT NULL,
    lastname VARCHAR(255) DEFAULT NULL,
    studentyear VARCHAR(50) DEFAULT NULL,
    gender VARCHAR(10) DEFAULT NULL,
    coursecode VARCHAR(50) DEFAULT NULL,
    FOREIGN KEY (coursecode) REFERENCES Courses(coursecode) ON DELETE CASCADE
);
