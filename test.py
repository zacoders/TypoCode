





        for name, generator_cls in inspect.getmembers(generators):
            if inspect.isclass(generator_cls) and issubclass(generator_cls, BaseGenerator):
                self.add_button(
                    Button(self.__buttons_size, name, action=lambda gen=generator_cls(): self.set_generator(gen))
                )