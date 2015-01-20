import re,os,sys,mercurial

def prefix_commit_message(repo, **kwargs):
 commitctx = repo.commitctx

 def rewrite_ctx(ctx, error):
   branch_name = ctx.branch()
   old_text = ctx._text
   if branch_name.startswith('ISB-'):
        ctx._text = branch_name+" "+old_text

   return commitctx(ctx, error)

 repo.commitctx = rewrite_ctx