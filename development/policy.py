import logging
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_nlu.components import ComponentBuilder


logger = logging.getLogger(__name__)

class StatusPolicy(KerasPolicy):
    def _build_model(self, num_features, num_actions, max_history_len):
        from keras.layers import LSTM, Activation, Masking, Dense
        from keras.models import Sequential

        n_hidden = 64
        model = Sequential()
        model.add(
            Masking(
                -1,
                batch_input_shape=(
                    None,
                    max_history_len,
                    num_features
                )
            )
        )
        model.add(LSTM(n_hidden, batch_input_shape=(
            None, max_history_len, num_features)))
        model.add(Dense(input_dim=n_hidden, output_dim=num_actions))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                      optimizer='adagrad',
                      metrics=['accuracy'])
        logger.debug(model.summary())
        return model
