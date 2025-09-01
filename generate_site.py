import os
from zipfile import ZipFile

# Create a folder structure and files for the website
base_dir = "huddle-up-media"
os.makedirs(base_dir, exist_ok=True)

# File contents
files = {
    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Huddle Up Media - The HUM</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <div class="logo">The HUM</div>
    <nav>
       <a href="index.html">Home</a>
      <a href="about.html">About</a>
       <a href="blog.html">Blog</a>
      <a href="media.html">Media</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Welcome to The HUM</h1>
    <p>Real life coaches talking about real life coaching.</p>
    <a href="media.html" class="btn">Explore Media</a>
  </section>

  <footer>
    <p>&copy; 2025 Huddle Up Media. All rights reserved.</p>
  </footer>
</body>
</html>""",

    "about.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>About - The HUM</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <div class="logo">The HUM</div>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="media.html">Media</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="page">
    <h2>About Huddle Up Media</h2>
    <p>The HUM is more than just a media outlet — it's a movement. We bring the latest in sports coaching philosophy, leadership development, and real talk from the sidelines. Whether you're a coach, athlete, or fan of the game, we’re here to elevate your mindset and game plan.</p>
  </section>

  <footer>
    <p>&copy; 2025 Huddle Up Media. All rights reserved.</p>
  </footer>
</body>
</html>""",

    "media.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Media - The HUM</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <div class="logo">The HUM</div>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="media.html">Media</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="page">
    <h2>Latest Media</h2>
    <ul class="media-list">
      <li><strong>🎧 Podcast:</strong> Leadership Lessons from the Locker Room</li>
      <li><strong>📺 Video:</strong> 3 Mental Tricks Pro Athletes Use</li>
      <li><strong>📝 Article:</strong> The Playbook to Building Team Culture</li>
    </ul>
  </section>

  <footer>
    <p>&copy; 2025 Huddle Up Media. All rights reserved.</p>
  </footer>
</body>
</html>""",

    "contact.html": """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Contact - The HUM</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <header>
    <div class="logo">The HUM</div>
    <nav>
      <a href="index.html">Home</a>
      <a href="about.html">About</a>
      <a href="media.html">Media</a>
      <a href="contact.html">Contact</a>
    </nav>
  </header>

  <section class="page">
    <h2>Contact Us</h2>
    <p>Email us: <a href="mailto:info@huddleupmedia.com">info@huddleupmedia.com</a></p>
    <p>Follow us on:
      <a href="#">Instagram</a> |
      <a href="#">YouTube</a> |
      <a href="#">X (Twitter)</a>
    </p>
  </section>

  <footer>
    <p>&copy; 2025 Huddle Up Media. All rights reserved.</p>
  </footer>
</body>
</html>""",

    "styles.css": """/* Global Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Open Sans', sans-serif;
  background-color: #f5f5f5;
  color: #222;
  line-height: 1.6;
}

header {
  background-color: #001f3f;
  color: white;
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  letter-spacing: 2px;
}

nav a {
  color: white;
  margin-left: 20px;
  text-decoration: none;
  font-weight: bold;
}

.hero {
  background-color: #0074D9;
  color: white;
  text-align: center;
  padding: 80px 20px;
}

.hero h1 {
  font-size: 48px;
  margin-bottom: 20px;
}

.hero .btn {
  background-color: #FFDC00;
  color: #000;
  padding: 12px 24px;
  font-weight: bold;
  text-decoration: none;
  border-radius: 4px;
}

.page {
  padding: 60px 40px;
  max-width: 800px;
  margin: auto;
}

.media-list {
  list-style-type: none;
  padding-left: 0;
}

.media-list li {
  margin-bottom: 15px;
}

footer {
  background-color: #001f3f;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 40px;
}

/* Responsive */
@media (max-width: 768px) {
  header {
    flex-direction: column;
    text-align: center;
  }

  nav {
    margin-top: 10px;
  }

  .hero h1 {
    font-size: 32px;
  }
}"""
}

# Create and write files
for filename, content in files.items():
    with open(os.path.join(base_dir, filename), "w", encoding="utf-8") as f:
        f.write(content)

# Zip the folder
with ZipFile(f"{base_dir}.zip", "w") as zipf:
    for root, _, files_in_dir in os.walk(base_dir):
        for file in files_in_dir:
            filepath = os.path.join(root, file)
            zipf.write(filepath, os.path.relpath(filepath, base_dir))

print("✅ Website files and ZIP archive created!")

