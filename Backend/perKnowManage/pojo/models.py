"""
encoding:   -*- coding: utf-8 -*-
@Time           :  2025/2/26 13:03
@Project_Name   :  PerKnowManage
@Author         :  lhw
@File_Name      :  models.py

功能描述

实现步骤

"""
from perKnowManage.config import db


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())
    login_ts = db.Column(db.TIMESTAMP, default=db.func.current_timestamp())


class Documents(db.Model):
    __tablename__ = 'documents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    file_path = db.Column(db.String(500), nullable=False)
    file_tag = db.Column(db.String(20), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    upload_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    update_time = db.Column(db.DateTime, default=db.func.current_timestamp())
    __table_args__ = (
        db.Index('ft_content', 'title', 'content', mysql_prefix='FULLTEXT'),
    )
    user = db.relationship('Users', backref=db.backref('documents', lazy=True))


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user = db.relationship('Users', backref=db.backref('tags', lazy=True))


document_tags = db.Table('document_tags',
                         db.Column('document_id', db.Integer, db.ForeignKey('documents.id'), primary_key=True),
                         db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'), primary_key=True)
                         )


class Entities(db.Model):
    __tablename__ = 'entities'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.Enum('Person', 'Location', 'Concept', 'Event'), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    __table_args__ = (
        db.Index('idx_name', 'name'),
    )


class Relationships(db.Model):
    __tablename__ = 'relationships'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_id = db.Column(db.Integer, db.ForeignKey('entities.id'), nullable=False)
    target_id = db.Column(db.Integer, db.ForeignKey('entities.id'), nullable=False)
    relation_type = db.Column(db.String(50), nullable=False)
    weight = db.Column(db.Float, default=1.0)
    source = db.relationship('Entities', foreign_keys=[source_id], backref=db.backref('outgoing_relationships', lazy=True))
    target = db.relationship('Entities', foreign_keys=[target_id], backref=db.backref('incoming_relationships', lazy=True))
    __table_args__ = (
        db.Index('idx_source_target', 'source_id', 'target_id'),
    )
