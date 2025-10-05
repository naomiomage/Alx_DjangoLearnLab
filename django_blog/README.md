\# Django Blog - Comment System



\## Features

\- Users can view comments on blog posts.

\- Authenticated users can create, edit, and delete their comments.

\- Comments are displayed in reverse chronological order under each post.



\## Models

\*\*Comment\*\*

\- post (ForeignKey to Post)

\- author (ForeignKey to User)

\- content (TextField)

\- created\_at (DateTimeField)

\- updated\_at (DateTimeField)



\## Permissions

\- Only authenticated users can add comments.

\- Only the comment author can edit or delete their own comment.

\- Comments are visible to everyone.



\## URLs

| URL | View | Description |

|-----|------|-------------|

| `/post/<post\_id>/comments/new/` | `CommentCreateView` | Create a new comment |

| `/comments/<pk>/edit/` | `CommentUpdateView` | Edit a comment |

| `/comments/<pk>/delete/` | `CommentDeleteView` | Delete a comment |



\## Testing

Run all tests with:

```bash

python manage.py test





\## Tagging and Search



\### Tags

\- Add tags when creating/editing a post using a comma-separated list.

\- Tags are stored in `Tag` model and linked via M2M to `Post`.

\- Tag pages: `/tags/<tag\_name>/` shows posts for that tag.



\### Search

\- Access search via `/search/?q=keyword`

\- Searches title, content, and tag names.



