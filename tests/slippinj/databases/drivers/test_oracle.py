import logging
from mock import Mock
from slippinj.databases.drivers.oracle import Oracle


class TestOracle:

    def setup_method(self, method):
        self.logger = logging.getLogger('test')

        self.logger.addHandler(logging.NullHandler())

    def teardown_method(self,method):
        self.logger = None

    def test_get_tables_info_when_no_table_list_is_provided(self):
        mocked_table_list_query_cursor = Mock()
        mocked_table_list_query_cursor.execute = Mock(return_value=True)
        mocked_table_list_query_cursor.fetchall = Mock(return_value=[{0: 'unit'}, {0: 'test'}])

        mocked_table_count_query_cursor = Mock()
        mocked_table_count_query_cursor.execute = Mock(return_value=True)
        mocked_table_count_query_cursor.fetchone = Mock(return_value=[10])

        columns = {
            0: '',
            1: 'column',
            2: 'string',
            3: '1',
            4: 'N',
            5: '',
        }
        tables_columns = []
        columns[0] = 'unit'
        tables_columns.append(columns.copy())
        columns[0] = 'test'
        tables_columns.append(columns.copy())
        mocked_table_columns_query_cursor = Mock()
        mocked_table_columns_query_cursor.execute = Mock(return_value=True)
        mocked_table_columns_query_cursor.fetchall = Mock(return_value=tables_columns)

        mocked_table_top_query_cursor = Mock()
        mocked_table_top_query_cursor.execute = Mock(return_value=True)
        mocked_table_top_query_cursor.fetchall = Mock(return_value=[])

        mocked_oracle = Mock()
        mocked_oracle.cursor = Mock(side_effect=[mocked_table_list_query_cursor, mocked_table_count_query_cursor,
                                                mocked_table_columns_query_cursor, mocked_table_top_query_cursor])
        mocked_builder = Mock()
        mocked_builder.build = Mock(return_value=mocked_oracle)

        expected = {'tables': {'test': {'columns': [{'character_maximum_length': '1',
                                                     'column_default': '',
                                                     'column_name': 'column',
                                                     'data_type_original': 'string',
                                                     'data_type': 'string',
                                                     'is_nullable': 'N'}],
                                        'count': 10,
                                        'rows': []},
                               'unit': {'columns': [{'character_maximum_length': '1',
                                                     'column_default': '',
                                                     'column_name': 'column',
                                                     'data_type_original': 'string',
                                                     'data_type': 'string',
                                                     'is_nullable': 'N'}],
                                        'count': 10,
                                        'rows': []}}}

        assert expected == Oracle(mocked_builder, self.logger).get_all_tables_info(None, None, None)

    def test_get_tables_info_when_table_list_has_been_provided(self):
        mocked_table_list_query_cursor = Mock()
        mocked_table_list_query_cursor.execute = Mock(return_value=True)
        mocked_table_list_query_cursor.fetchall = Mock(return_value=[{0: 'test'}])

        mocked_table_count_query_cursor = Mock()
        mocked_table_count_query_cursor.execute = Mock(return_value=True)
        mocked_table_count_query_cursor.fetchone = Mock(return_value=[10])

        columns = {
            0: '',
            1: 'column',
            2: 'string',
            3: '1',
            4: 'N',
            5: '',
        }
        tables_columns = []
        columns[0] = 'unit'
        tables_columns.append(columns.copy())
        columns[0] = 'test'
        tables_columns.append(columns.copy())
        mocked_table_columns_query_cursor = Mock()
        mocked_table_columns_query_cursor.execute = Mock(return_value=True)
        mocked_table_columns_query_cursor.fetchall = Mock(return_value=tables_columns)

        mocked_table_top_query_cursor = Mock()
        mocked_table_top_query_cursor.execute = Mock(return_value=True)
        mocked_table_top_query_cursor.fetchall = Mock(return_value=[])

        mocked_oracle = Mock()
        mocked_oracle.cursor = Mock(side_effect=[mocked_table_list_query_cursor, mocked_table_count_query_cursor, mocked_table_columns_query_cursor, mocked_table_top_query_cursor])
        mocked_builder = Mock()
        mocked_builder.build = Mock(return_value=mocked_oracle)

        expected = {'excluded_tables': ['test'], 'tables': {
            'unit': {'columns': [{'character_maximum_length': '1',
                                  'column_default': '',
                                  'column_name': 'column',
                                  'data_type_original': 'string',
                                  'data_type': 'string',
                                  'is_nullable': 'N'}],
                     'count': 10,
                     'rows': []}}}

        assert expected == Oracle(mocked_builder, self.logger).get_all_tables_info('unit', None, None)
