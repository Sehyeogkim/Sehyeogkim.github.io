# Add anchors to archived HTML headings at render time without modifying source bodies.
require 'nokogiri'
Jekyll::Hooks.register :posts, :pre_render do |post|
  next unless post.data['legacy_html']
  source = post.content
  used = source.scan(/\bid=["']([^"']+)["']/).flatten
  post.content = source.gsub(/<(h[2-6])([^>]*)>(.*?)<\/\1>/m) do
    original = Regexp.last_match(0)
    tag, attributes, body = Regexp.last_match.captures
    next original if attributes.match?(/\bid\s*=/)
    title = Nokogiri::HTML.fragment(body).text
    base = title.strip.empty? ? 'section' : Jekyll::Utils.slugify(title, mode: 'default')
    base = 'section' if base.empty?
    id = base
    suffix = 1
    while used.include?(id)
      id = "#{base}-#{suffix}"
      suffix += 1
    end
    used << id
    "<#{tag}#{attributes} id=\"#{id}\">#{body}</#{tag}>"
  end
end
