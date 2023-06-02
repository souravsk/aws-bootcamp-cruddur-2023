from lib.db import db

class ReplyToActivityUuidToStringMigration:
  def migrate_sql():
    data = """
    """
    return data
  def rollback_sql():
    data = """
    """
    return data

  def migrate():
    db.query_commit(ReplyToActivityUuidToStringMigration.migrate_sql(),{
    })

  def rollback():
    db.query_commit(ReplyToActivityUuidToStringMigration.rollback_sql(),{
    })

migration = ReplyToActivityUuidToStringMigration