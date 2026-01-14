class AdminPageLocators:
    # Header / navigation
    ADMIN_DASHBOARD_LINK = "a[href='/admin']"

    # Blog list and actions
    BLOG_CARD = "div[data-testid='admin-blog-card']"
    BLOG_TITLE_IN_CARD = "h6"  # adjust if needed
    DELETE_BUTTON_IN_CARD = "button[aria-label='Delete']"
    CONFIRM_DELETE_BUTTON = "button:has-text('Delete')"
    CANCEL_DELETE_BUTTON = "button:has-text('Cancel')"

    # Create / edit blog
    CREATE_BLOG_BUTTON = "a[href='/admin/blogs/new'], button:has-text('New Post')"
    TITLE_INPUT = "input[label='Title'], input[name='title'], input[id='title']"
    EXCERPT_INPUT = "textarea[label='Excerpt'], textarea[name='excerpt']"
    CATEGORY_SELECT = "div[role='button'][id*='category'], div[role='button'][aria-haspopup='listbox']"
    CATEGORY_OPTION = "li.MuiMenuItem-root"
    TAGS_SELECT = "div[role='button'][id*='tags']"
    TAG_OPTION = "li.MuiMenuItem-root"
    IMAGE_UPLOAD_INPUT = "input[type='file']"
    SAVE_BUTTON = "button:has-text('Save')"
    PUBLISH_NOW_BUTTON = "button:has-text('Publish Now')"

    # Status chip in admin list
    STATUS_CHIP_PUBLISHED = "span.MuiChip-label:has-text('Published')"
    STATUS_CHIP_DRAFT = "span.MuiChip-label:has-text('Draft')"

