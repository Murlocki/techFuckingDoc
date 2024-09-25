import models.functions
class MainWindowController:
    def __init__(self, window):
        self._window = window
        self.labController = None
        self.function = None
        self.z_scale = None
        self.gridOn = True
        self.axisOn = True
        self.ticklabelsOn = True
        self.x_start = None
        self.y_start = None
    @property
    def window(self):
        return self._window
    @window.setter
    def window(self, new):
        self._window = new
    def x_interval_getter(self) -> str:
        return self.window.x_interval.text()
    def y_interval_getter(self) -> str:
        return self.window.y_interval.text()
    def z_scale_getter(self) -> float:
        self.z_scale = float(self.window.z_scale.text())
        return self.z_scale
    def grid_change(self):
        self.gridOn = self.window.grid.isChecked()
        self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn,self.ticklabelsOn)
        return self.gridOn
    def axes_change(self):
        self.axisOn = self.window.axes.isChecked()
        self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn,self.ticklabelsOn)
        return self.axisOn
    def ticklabels_changed(self):
        self.ticklabelsOn = self.window.ticklabels.isChecked()
        self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn,self.ticklabelsOn)
        return self.ticklabelsOn
    def x_interval_changed(self):
        self.functions_selector()
    def y_interval_changed(self):
        self.functions_selector()
    def z_scale_changed(self):
        self.functions_selector()
    def text_output_append(self, text):
        self.window.textOutput.append(text)
    def text_output_clear(self):
        self.window.textOutput.clear()
    def function_setter(self, function):
        self.function = function
        self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn, self.ticklabelsOn)
    def clear_all(self):
        self.text_output_clear()
        self.window.graph.clear_points()
    def functions_selector(self):
        selected_function = self.window.functionSelector.currentText()
        if selected_function == 'Функция Матьяса':
            self.function = models.functions.MatiasFunction(x_interval_str=self.x_interval_getter(),y_interval_str=self.y_interval_getter())
        elif selected_function == 'Функция верблюда':
            self.function = models.functions.CamelThreeHumpFunction(x_interval_str=self.x_interval_getter(),y_interval_str=self.y_interval_getter())
        elif selected_function == 'Функция Розенброка':
            self.function = models.functions.RosenbrockFunction(x_interval_str=self.x_interval_getter(),y_interval_str=self.y_interval_getter())
        self.labController.set_function(self.function)
        self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn,self.ticklabelsOn)
    def get_current_function(self):
        return self.function
    def lab_selector(self):
        current_tab = self.window.tabWidget.currentWidget()
        self.window.functionSelector.setEnabled(True)
        if current_tab == self.window.tab_lab1:
            self.labController = self.window.lab1_controller
            self.functions_selector()
        elif current_tab == self.window.tab_lab3:
            self.window.functionSelector.setEnabled(False)
            self.function_setter(models.functions.RosenbrockFunction())
            self.window.updateGraph(self.function.get_function(), self.z_scale_getter(), self.gridOn, self.axisOn,self.ticklabelsOn)
            self.labController = self.window.lab3_controller
