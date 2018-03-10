angular.module('mwl.calendar.docs', ['mwl.calendar', 'ngAnimate', 'ui.bootstrap', 'colorpicker.module']);
angular
  .module('mwl.calendar.docs')
  .controller('RecurringEventsCtrl', function($scope, moment, calendarConfig) {

    var vm = this;

    vm.events = [];
    vm.events2 = [];
    vm.eventsAux =[];
    vm.calendarView = 'month';
    vm.viewDate = moment().toDate();
    vm.cellIsOpen = true;

        var actions = [{
      label: '<i class=\'glyphicon glyphicon-pencil\'></i>',
      onClick: function(args) {
        alert.show('Edited', args.calendarEvent);
      }
    }, {
      label: '<i class=\'glyphicon glyphicon-remove\'></i>',
      onClick: function(args) {
        alert.show('Deleted', args.calendarEvent);
      }
    }];
    vm.events = [
      
    ];
        vm.events2 = [
      
    ];
            vm.calendarView = 'month';
    vm.viewDate = new Date();
vm.viewChangeClicked = function(nextView) {
      if (nextView === 'day') {
        return false;
      }
    };
        vm.addEvent = function() {
      vm.events.push({
        title: 'Día inhábil',
        startsAt: moment().startOf('day').toDate(),
        endsAt: moment().endOf('day').toDate(),
        color: calendarConfig.colorTypes.Tec,
        draggable: true,
        resizable: true
      });
    };

            vm.addEvent2 = function() {

vm.events.push({
        title: 'Día inhábil',
        startsAt: moment().startOf('day').toDate(),
        endsAt: moment().endOf('day').toDate(),
        color: calendarConfig.colorTypes.Tec,
        draggable: true,
        resizable: true
      }),

      vm.events2.push({
        title: 'Día inhábil',
        startsAt: moment().startOf('day').toDate(),
        endsAt: moment().endOf('day').toDate(),
        color: calendarConfig.colorTypes.Tec,
        draggable: true,
        resizable: true
      }


      );
    };



        vm.BorrarEvent = function() {

      vm.events = vm.eventsAux.concat(vm.events2);

    };





     vm.eventClicked = function(event) {
      alert.show('Clicked', event);
    };

    vm.eventEdited = function(event) {
      alert.show('Edited', event);
    };

    vm.eventDeleted = function(event) {
      alert.show('Deleted', event);
    };

    vm.eventTimesChanged = function(event) {
      alert.show('Dropped or resized', event);
    };

    vm.toggle = function($event, field, event) {
      $event.preventDefault();
      $event.stopPropagation();
      event[field] = !event[field];
    };

    var events = [{
      title: 'Día inhábil',
      color: calendarConfig.colorTypes.Tec,
      rrule: {
        freq: RRule.WEEKLY,
        byweekday: [RRule.SU],
      }
    },
{
      title: 'Día inhábil',
      color: calendarConfig.colorTypes.Tec,
      rrule: {
        freq: RRule.WEEKLY,
        byweekday: [RRule.SA],
      }
    }
    ];

    $scope.$watchGroup([
      'vm.calendarView',
      'vm.viewDate'
    ], function() {

      vm.events = [];

      events.forEach(function(event) {

        // Use the rrule library to generate recurring events: https://github.com/jkbrzt/rrule
        var rule = new RRule(angular.extend({}, event.rrule, {
          dtstart: moment(vm.viewDate).startOf(vm.calendarView).toDate(),
          until: moment(vm.viewDate).endOf(vm.calendarView).toDate()
        }));

        rule.all().forEach(function(date) {
          vm.events.push(angular.extend({}, event, {
            startsAt: new Date(date)
          }

          ));
vm.eventsAux.push(angular.extend({}, event, {
            startsAt: new Date(date)
          }

          ));

        });

      });

    });

    vm.timespanClicked = function(date, cell) {

      if (vm.calendarView === 'month') {
        if ((vm.cellIsOpen && moment(date).startOf('day').isSame(moment(vm.viewDate).startOf('day'))) || cell.events.length === 0 || !cell.inMonth) {
          vm.cellIsOpen = false;
        } else {
          vm.cellIsOpen = true;
          vm.viewDate = date;
        }
      } else if (vm.calendarView === 'year') {
        if ((vm.cellIsOpen && moment(date).startOf('month').isSame(moment(vm.viewDate).startOf('month'))) || cell.events.length === 0) {
          vm.cellIsOpen = false;
        } else {
          vm.cellIsOpen = true;
          vm.viewDate = date;
        }
      }

    };

  });