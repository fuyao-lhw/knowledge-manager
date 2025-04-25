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

# 实体表
class Entities(db.Model):
    __tablename__ = 'entities'
    entity_id = db.Column(db.Integer, primary_key=True)
    entity_name = db.Column(db.String(255), nullable=False)
    entity_type = db.Column(db.String(50), nullable=False)


# 关系信息表
class RelationshipsInfo(db.Model):
    __tablename__ = 'relationships_info'
    relationship_id = db.Column(db.Integer, primary_key=True)
    relationship_name = db.Column(db.String(100), unique=True, nullable=False)


# 实体关系表
class EntityRelationships(db.Model):
    __tablename__ = 'entity_relationships'
    entity_relationship_id = db.Column(db.Integer, primary_key=True)
    entity1_id = db.Column(db.Integer, db.ForeignKey('entities.entity_id', ondelete='CASCADE'))
    entity2_id = db.Column(db.Integer, db.ForeignKey('entities.entity_id', ondelete='CASCADE'))
    relationship_id = db.Column(db.Integer, db.ForeignKey('relationships_info.relationship_id', ondelete='CASCADE'))
    entity1 = db.relationship('Entities', foreign_keys=[entity1_id],
                              backref=db.backref('outgoing_relationships', cascade='all, delete-orphan'))
    entity2 = db.relationship('Entities', foreign_keys=[entity2_id],
                              backref=db.backref('incoming_relationships', cascade='all, delete-orphan'))
    relationship = db.relationship('RelationshipsInfo',
                                   backref=db.backref('entity_relationships', cascade='all, delete-orphan'))

# 属性表
class Attributes(db.Model):
    __tablename__ = 'attributes'
    attribute_id = db.Column(db.Integer, primary_key=True)
    attribute_name = db.Column(db.String(100), nullable=False)
    attribute_value = db.Column(db.Text)
    entity_id = db.Column(db.Integer, db.ForeignKey('entities.entity_id', ondelete='CASCADE'))
    entity = db.relationship('Entities', backref=db.backref('attributes', cascade='all, delete-orphan'))

# 同义词表
class Synonyms(db.Model):
    __tablename__ = 'synonyms'
    synonym_id = db.Column(db.Integer, primary_key=True)
    main_word = db.Column(db.String(255), nullable=False)
    synonym_word = db.Column(db.String(255), nullable=False)
