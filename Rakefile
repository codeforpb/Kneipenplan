require "rubygems"
require 'rake'
require 'yaml'
require 'time'

SOURCE = "."
CONFIG = {
  'version' => "0.3.0",
  'posts' => File.join(SOURCE, "_posts"),
  'bars' => File.join(SOURCE, "bars/_posts"),
  'food' => File.join(SOURCE, "food/_posts"),
  'post_ext' => "md",
  'theme_package_version' => "0.1.0"
}

# Path configuration helper
module JB
  class Path
    SOURCE = "."
    Paths = {
      :food => "food/_posts",
      :bars => "bars/_posts"
    }

    def self.base
      SOURCE
    end

    # build a path relative to configured path settings.
    def self.build(path, opts = {})
      opts[:root] ||= SOURCE
      path = "#{opts[:root]}/#{Paths[path.to_sym]}/#{opts[:node]}".split("/")
      path.compact!
      File.__send__ :join, path
    end

  end #Path
end #JB

# Usage: rake bar name="A name" [date="2012-02-09"] [lat="51.7..."] [lon="8.7..."]
desc "Add a new bar in #{CONFIG['bars']}"
task :bar do
  abort("rake aborted: '#{CONFIG['bars']}' directory not found.") unless FileTest.directory?(CONFIG['bars'])
  name = ENV["name"] || "new-bar"
  if ENV["lat"].to_f.between?(51.6,51.8)
      lat = ENV["lat"]
  else
      lat = ""
  end

  if ENV["lon"].to_f.between?(8.6,8.9)
      lon = ENV["lon"]
  else
      lon = ""
  end

  slug = name.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
  begin
    date = (ENV['date'] ? Time.parse(ENV['date']) : Time.now).strftime('%Y-%m-%d')
  rescue => e
    puts "Error - date format must be YYYY-MM-DD, please check you typed it correctly!"
    exit -1
  end
  filename = File.join(CONFIG['bars'], "#{date}-#{slug}.#{CONFIG['post_ext']}")
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end

  puts "Creating new bar: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "name: \"#{name.gsub(/-/,' ')}\""
    post.puts 'special: ""'
    post.puts "lat: #{lat}"
    post.puts "lon: #{lon}"
    post.puts "---"
  end
end # task :bar

# Usage: rake food name="A name" [date="2012-02-09"] [lat="51.7..."] [lon="8.7..."]
desc "Add a new fressbude in #{CONFIG['food']}"
task :food do
  abort("rake aborted: '#{CONFIG['food']}' directory not found.") unless FileTest.directory?(CONFIG['food'])
  name = ENV["name"] || "new-fressbude"
  if ENV["lat"].to_f.between?(51.6,51.8)
      lat = ENV["lat"]
  else
      lat = ""
  end

  if ENV["lon"].to_f.between?(8.6,8.9)
      lon = ENV["lon"]
  else
      lon = ""
  end

  slug = name.downcase.strip.gsub(' ', '-').gsub(/[^\w-]/, '')
  begin
    date = (ENV['date'] ? Time.parse(ENV['date']) : Time.now).strftime('%Y-%m-%d')
  rescue => e
    puts "Error - date format must be YYYY-MM-DD, please check you typed it correctly!"
    exit -1
  end
  filename = File.join(CONFIG['food'], "#{date}-#{slug}.#{CONFIG['post_ext']}")
  if File.exist?(filename)
    abort("rake aborted!") if ask("#{filename} already exists. Do you want to overwrite?", ['y', 'n']) == 'n'
  end

  puts "Creating new fressbude: #{filename}"
  open(filename, 'w') do |post|
    post.puts "---"
    post.puts "name: \"#{name.gsub(/-/,' ')}\""
    post.puts 'special: ""'
    post.puts "lat: #{lat}"
    post.puts "lon: #{lon}"
    post.puts "---"
  end
end # task :food



def ask(message, valid_options)
  if valid_options
    answer = get_stdin("#{message} #{valid_options.to_s.gsub(/"/, '').gsub(/, /,'/')} ") while !valid_options.include?(answer)
  else
    answer = get_stdin(message)
  end
  answer
end

def get_stdin(message)
  print message
  STDIN.gets.chomp
end
