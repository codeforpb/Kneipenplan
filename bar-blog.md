---
layout: default
---

<div class="home">

  <h1>Posts</h1>

  <ul class="posts">
    {% for post in site.categories.bars %}
      <li>
        <span class="post-date">{{ post.date | date: "%b %-d, %Y" }}</span>
        <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.name }}</a>
        <p><span class="special">{{ post.special }}</span><br/>{{ post.content | remove: '<p>' | remove: '</p>'}}</p>
      </li>
    {% endfor %}
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>