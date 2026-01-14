class BlogPageLocators:
    # Public home / list page
    BLOG_CARD = "article[data-testid='blog-card'], div[data-testid='blog-card']"
    BLOG_CARD_TITLE = "h5, h6"
    SEARCH_INPUT = "input[placeholder*='Search'], input[type='search']"
    SEARCH_BUTTON = "button:has-text('Search')"

    # Theme toggle and read state
    THEME_TOGGLE = "button[aria-label*='theme'], input[type='checkbox'][name='theme']"
    READ_BADGE = "[data-testid='read-badge']"

    # Pagination
    NEXT_PAGE_BUTTON = "button[aria-label='Go to next page'], button:has-text('Next')"
    PAGE_BUTTON = "button[aria-label='Go to page'], button.MuiPaginationItem-root"
    ACTIVE_PAGE = "button[aria-current='true'], button.Mui-selected"

    # Blog detail page
    BLOG_TITLE = "h1, h2"
    BLOG_CONTENT = "div.ql-editor"
    LIKE_BUTTON = "button:has-text('Like'), button[aria-label='like']"
    LIKE_COUNT = "[data-testid='like-count']"

    COMMENT_INPUT = "textarea[placeholder*='comment'], textarea[name='comment']"
    COMMENT_SUBMIT = \"button:has-text('Comment'), button:has-text('Post Comment')\"
    COMMENT_ITEM = \"[data-testid='comment-item']\"

