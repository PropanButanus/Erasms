odoo.define('custom_snippets.explore_jobs', function (require) {
  'use strict';

  var core = require('web.core');
  var Widget = require('web.Widget');
  var sAnimations = require('website.content.snippets.animation');

  var QWeb = core.qweb;

  var OwlCarousel = Widget.extend({
    selector: '.owl-carousel',

    start: function () {
      this.$el.owlCarousel({
        items: 1,
        nav: true,
        navText: [
          '<i class="fa fa-angle-left"></i>',
          '<i class="fa fa-angle-right"></i>'
        ],
        lazyLoad: true,
        loop: true,
        autoplay: true,
        autoplayTimeout: 3000,
        autoplayHoverPause: true
      });
    }
  });

  sAnimations.registry.owlCarousel = sAnimations.Animation.extend({
    selector: '.owl-carousel',

    start: function () {
      return new OwlCarousel(this).attachTo(this.$el);
    }
  });

  return {
    OwlCarousel: OwlCarousel
  };
});
