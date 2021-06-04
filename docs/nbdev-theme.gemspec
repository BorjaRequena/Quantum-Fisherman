# frozen_string_literal: true

Gem::Specification.new do |spec|
  spec.name          = "nbdev-jekyll-theme"
  spec.version       = "0.1.0"
  spec.authors       = ["Hamel Husain", "Jeremy Howard", "Sylvain Gugger"]
  spec.email         = ["info@fast.ai"]

  spec.summary       = "A docs theme made for nbdev: https://nbdev.fast.ai/"
  spec.homepage      = "https://github.com/fastai/nbdev-jekyll-theme"
  spec.license       = "Apache Version 2.0"

  spec.files         = `git ls-files -z`.split("\x0").select { |f| f.match(%r!^(assets|_layouts|_includes|_sass|LICENSE|README|_config\.yml)!i) }

  spec.add_runtime_dependency "jekyll", ">= 3.7"
  spec.add_runtime_dependency "nokogiri"
  spec.add_runtime_dependency "kramdown", ">= 2.3.0"
end
