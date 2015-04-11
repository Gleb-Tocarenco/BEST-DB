var app = {}

app.Todo = Backbone.Model.extend({
  defaults: {
    title: '',
    completed: false
  }
})

app.TodoList = Backbone.Collection.extend({
  model: app.Todo,
  localStorage: new Store('backbone-todo')
})

app.todoList = new app.TodoList();

app.TodoView = Backbone.View.extend({
  tagName: 'li',
  template: _.template($('#item-template').html()),
  render: function(){
    this.$el.html(this.template(this.model.toJSON()));
    return this;
  }
})

app.AppView = Backbone.View.extend({
  el: '#todoapp',
  initialize: function(){
    this.input = this.$('#new-todo');
    app.todoList.on('add', this.addAll, this);
    app.todoList.on('reset', this.addAll, this);
    app.todoList.fetch();
  },
  events: {
    'keypress #new-todo': 'createTodoOnEnter'
  },
  createTodoOnEnter: function(e){
    if( e.which !== 13 || !this.input.val().trim() ){
      return ;
    }
    app.todoList.create(this.newAttributes());
    this.input.val('')
  },
  addOne: function(todo){
    var view = new app.TodoView({model: todo})
    $('#todo-list').append(view.render().el);
  },
  addAll: function(){
    this.$('#todo-list').html('');
    app.todoList.each(this.addOne, this);
  },
  newAttributes: function(){
    return {
      title: this.input.val().trim(),
      completed: false
    }
  }
});



app.appView = new app.AppView();