import React from 'react';
import MatchForm from 'components/admin/MatchForm.jsx';
import { postSingleMatch, postSingleGame } from 'services/api.js';

const SingleMatchAdd = () => (
  <MatchForm
    matchType="singles"
    postMatch={postSingleMatch}
    postGame={postSingleGame}
  />
);

export default SingleMatchAdd;