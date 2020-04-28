import Ember from 'ember';
import Browser from '../models/browser';
import Version from '../models/version';

export default Ember.Route.extend({
  model: function() {
    return this.store.findAll('browser');
  },
  actions: {
    didTransition: function() {
      // update document title
      document.title = 'Browsers';
    },
  },
});
