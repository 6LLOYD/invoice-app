import React from 'react';
import { Tabs, TabList, Tab, TabPanel } from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import Devis from './Devis';
// import Facture from './Facture';

const AppTabs: React.FC = () => {
  return (
    <Tabs>
      <TabList className="nav nav-tabs">
        <Tab className="nav-link" selectedClassName="nav-link active">
          Devis
        </Tab>
        <Tab className="nav-link" selectedClassName="nav-link active">
          Facture
        </Tab>
      </TabList>

      <TabPanel>
        <Devis />
      </TabPanel>
      <TabPanel>
        {/* <Facture /> */}
      </TabPanel>
    </Tabs>
  );
};

export default AppTabs;