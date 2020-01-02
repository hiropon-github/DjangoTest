from django.db import models

class Todo(models.Model):
    todo = models.CharField('Todo', max_length=100, blank=False)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    
    # テーブル名を設定
    class Meta:
        db_table = 'todo_list'

    def __str__(self):
        return self.todo